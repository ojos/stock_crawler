# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

from flask import Flask, request

from .stock.api import StockApi

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello Stock Crawler"


@app.route('/__cron__/stocks', methods=['GET'])
def crawl():
    api = StockApi()
    api.crawl()
    return "I'm Crawler!!"
