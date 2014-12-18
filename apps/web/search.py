#!/usr/bin/env python
# coding=utf-8

import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from apps.data.twitter_search import SearchTopicDAO
from apps.data.data_manage import DataManageDAO, DataCollectDAO


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        keyword = self.get_argument('keyword', None)
        if not keyword:
            self.render('error.html')
        cur_time = int(time.time())
        data = []
        if not SearchTopicDAO(keyword, cur_time).search():
            data = DataCollectDAO(keyword, cur_time).data_collect()
        data = DataManageDAO(keyword, cur_time).data_manage()
        return self.render('main.html', data=data)
