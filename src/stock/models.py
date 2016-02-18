# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from google.appengine.ext import ndb


class Stock(ndb.Model):
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    stock_id = ndb.StringProperty(required=True, indexed=True)
    title = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)
    tags = ndb.StringProperty(repeated=True)


class CurrentStock(ndb.Model):
    updated_at = ndb.DateTimeProperty(auto_now=True)
    stock_id = ndb.StringProperty(required=True)
