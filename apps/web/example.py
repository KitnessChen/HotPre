#!/usr/bin/env python
# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from data.data_manage import ExampleDAO

class ExampleHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('example.html')

    def post(self, url_token):
        if not url_token:
            return self.render('error.html')
        data = ExampleDAO.get_example(url_token)
        return data
