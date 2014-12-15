#!/usr/bin/env python
# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import options

from apps.web.search import SearchHandler
from apps.web.main import IndexHandler
from apps.web.sample import SampleHandler
from apps.predict.main import PredictHandler

from config.define import *

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/home", IndexHandler),
            (r"/predicit", PredictHandler),
            (r"/samples", SampleHandler),
            (r"/samples/(\w+)", SampleHandler),
            (r"/search", SearchHandler)
        ],
        template_path=options.template_path,
        static_path=options.static_path
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
