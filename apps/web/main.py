#!/usr/bin/env python
# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def render_json(self, template_name, **kwargs):
        self.set_header("Content-Type", "application/json")
        return self.render(template_name, **kwargs)


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')
