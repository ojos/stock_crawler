# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import json
import logging

from google.appengine.api import urlfetch

from ..crawlers.ping import Ping
from .models import Stock, CurrentStock


class StockApi(object):
    stock_api_url = 'https://qiita.com/api/v2/users/%s/stocks?page=%d&per_page=%d'
    stock_user = 'your_name'
    stock_count = 100

    def __init__(self):
        self.stock_page = 1

    def get_current_stock(self):
        current = CurrentStock.query().get()
        if current is None:
            current = CurrentStock()

        return current

    def get_stocks(self):
        url = self.stock_api_url % (self.stock_user, self.stock_page, self.stock_count)
        res = urlfetch.fetch(url=url,
                             method=urlfetch.GET,
                             headers={'Content-Type': 'application/x-www-form-urlencoded',
                                      'Cache-Control': 'max-age=0'})
        logging.debug(res.content)
        return json.loads(res.content)

    def crawl(self):
        crawler = Ping()
        current = self.get_current_stock()
        current_id = None

        while True:
            stocks = self.get_stocks()
            if len(stocks) == 0:
                if current_id is not None:
                    current.stock_id = current_id
                    current.put()
                break

            if self.stock_page == 1:
                current_id = stocks[0]['id']

            for s in stocks:
                if s['id'] == current.stock_id:
                    break
                else:
                    stock = Stock(stock_id=s['id'],
                                  title=s['title'],
                                  tags=[t['name'] for t in s['tags']],
                                  url=s['url'])
                    stock.put()
                    crawler.say(u'%s\n%s\n%s' % (stock.title,
                                                 u' / '.join(stock.tags),
                                                 stock.url))
            self.stock_page = self.stock_page + 1
