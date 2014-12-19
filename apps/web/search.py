#!/usr/bin/env python
# coding=utf-8

import time

from apps.data.twitter_search import SearchTopicDAO
from apps.data.data_manage import DataManageDAO, DataCollectDAO
from apps.web.main import BaseHandler


class SearchHandler(BaseHandler):
    def get(self):
        keyword = self.get_argument('keyword', None)
        if not keyword:
            return self.render_json('ajax/fail.json', error=u'No keyword')
        features = DataManageDAO.get_features()
        cur_time = int(time.time())
        return self.render('main.html', features=features, keyword=keyword, cur_time=cur_time)


class SearchDetailHandler(BaseHandler):
    def get(self, url_token):
        if not url_token:
            return self.render_json('ajax/fail.json', error=u'No keyword')
        _time = int(self.get_argument('cur_time', None))
        cur_time = time.localtime(_time)
        if not cur_time:
            return self.render_json('ajax/fail.json', error=u'No time')
        data = {}
        if not SearchTopicDAO(url_token, cur_time).search():
            data = DataCollectDAO(url_token, cur_time).data_collect()
        else:
            data = DataManageDAO(url_token, cur_time).data_manage()
        return self.render_json('ajax/success.json', msg=data)
