#!/usr/bin/env python
# coding=utf-8

import time

from apps.web.main import BaseHandler
from apps.data.data_manage import PredictDAO, SamplePredictDAO

class PredictHandler(BaseHandler):
    def get(self):
        keyword = self.get_argument('keyword', None)
        _time = int(self.get_argument('cur_time', None))
        cur_time = time.localtime(_time)
        if not keyword or not cur_time:
            return self.render_json('ajax/fail.json', error=u'')
        data = PredictDAO(cur_time, keyword).predict()
        hot_mark = PredictDAO(cur_time, keyword).get_hotmark()
        return self.render_json('ajax/success.json', msg={'data':data,'hot_mark':hot_mark})


class SamplePredictHandler(BaseHandler):
    def get(self):
        keyword = self.get_argument('keyword', None)
        if not keyword:
            return self.render_json('ajax/fail.json', error=u'')
        data = SamplePredictDAO(keyword).predict()
        hot_mark = SamplePredictDAO(keyword).get_hotmark()
        return self.render_json('ajax/success.json', msg={'data':data,'hot_mark':hot_mark})