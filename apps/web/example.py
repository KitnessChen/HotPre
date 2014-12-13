#!/usr/bin/env python
# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class ExamplesHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('example.html')

    def post(self):
        return True

    # need function detail
