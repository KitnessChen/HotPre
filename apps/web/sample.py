#!/usr/bin/env python
# coding=utf-8

from apps.data.data_manage import SampleDAO
from apps.web.main import BaseHandler

class SampleHandler(BaseHandler):
    def get(self):
        samples = SampleDAO.get_samples()
        features = SampleDAO.get_features()
        if not samples:
            return self.render_json('ajax/fail.json', error=u'')
        return self.render('sample.html', samples=samples, features=features)


class SampleDetailHandler(BaseHandler):
    def get(self, url_token=None):
        if not url_token:
            return self.render_json('ajax/fail.json', error=u'')
        data = SampleDAO.get_sample(keyword=url_token)
        return self.render_json('ajax/success.json', msg=data)
