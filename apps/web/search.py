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
        cur_time = int(time.time())
        data = []
        features = DataManageDAO.get_features()
        if not SearchTopicDAO(keyword, cur_time).search():
            data = DataCollectDAO(keyword, cur_time).data_collect()
        data = DataManageDAO(keyword, cur_time).data_manage()
        return self.render('main.html', data=data, features=features, keyword=keyword)
