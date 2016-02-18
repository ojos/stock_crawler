# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from . import BaseCrawler


class Ping(BaseCrawler):
    _NAME = 'Qiita Stock'
    _ICON = ':penguin:'
    _CHANNEL = '#dummy'
