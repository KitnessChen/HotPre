#!/usr/bin/env python
# coding=utf-8

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import options

from apps.web.search import SearchHandler, SearchDetailHandler
from apps.web.main import IndexHandler
from apps.web.sample import SampleHandler, SampleDetailHandler
from apps.predict.main import PredictHandler

from config.define import *

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/home", IndexHandler),
            (r"/predicit", PredictHandler),
            (r"/samples", SampleHandler),
            (r"/samples/([^/]+)", SampleDetailHandler),
            (r"/search", SearchHandler),
            (r"/search/([^/]+)", SearchDetailHandler)
        ],
        template_path=options.template_path,
        static_path=options.static_path
    )
    logger.info("Tornado HotPre server starting...")
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
