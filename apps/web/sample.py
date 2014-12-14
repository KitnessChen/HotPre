#!/usr/bin/env python
# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from data.data_manage import SampleDAO


class SampleHandler(tornado.web.RequestHandler):
    def get(self):
        samples = SampleDAO.get_samples()
        return self.render('sample.html', samples=samples)

    def post(self, url_token):
        if not url_token:
            return self.render('error.html')
        data = SampleDAO.get_sample(url_token)
        return data
