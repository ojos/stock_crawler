# coding: utf-8

from __future__ import absolute_import, division, print_function

import logging
import urllib

from google.appengine.api import urlfetch


class BaseCrawler(object):
    _ICON = ':slack:'
    _NAME = 'Slack'
    _URL = 'https://slack.com/api/chat.postMessage'
    _METHOD = urlfetch.POST
    _TOKEN = 'your-team-token'
    _CHANNEL = '#general'
    _MESSAGE = 'Hello!!'

    def build_payload(self, message=None, channel=None):
        return {'token': self._TOKEN,
                'channel': self._CHANNEL if channel is None else channel,
                'text': self._MESSAGE if message is None else message,
                'icon_emoji': self._ICON,
                'username': self._NAME
                }

    def say(self, message=None, channel=None):
        if message is not None:
            message = message.encode('utf-8')

        payload = urllib.urlencode(self.build_payload(message, channel))
        res = urlfetch.fetch(url=self._URL,
                             payload=payload,
                             method=self._METHOD,
                             headers={'Content-Type': 'application/x-www-form-urlencoded',
                                      'Cache-Control': 'max-age=0'})
        logging.debug(res.content)
        return ''
