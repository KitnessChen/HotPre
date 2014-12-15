#!/usr/bin/env python
# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

class PredictHandler(tornado.web.RequestHandler):
    def post(self):
        return True