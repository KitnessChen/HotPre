#!/usr/bin/env python
# coding=utf-8

import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from data.twitter_search import SearchTopic
from data.data_manage import DataManage


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        topic = self.get_argument('keyword', None)
        if not topic:
            self.render('error.html')
        cur_time = int(time.time())
        SearchTopic.search(topic, cur_time)
        DataManage.data_format(topic, cur_time)
        DataManage.data_collect(topic, cur_time)
        return self.render('success.html')
