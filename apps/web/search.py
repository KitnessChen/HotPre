#!/usr/bin/env python
# coding=utf-8

import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from data.twitter_search import SearchTopicDAO
from data.data_manage import DataManageDAO, DataCollectDAO


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        topic = self.get_argument('keyword', None)
        if not topic:
            self.render('error.html')
        cur_time = int(time.time())
        data = []
        if not SearchTopicDAO.search(topic, cur_time):
            data = DataCollectDAO.data_collect(topic, cur_time)
        data = DataManageDAO.data_manage(topic, cur_time)
        return self.render('main.html', data=data)
