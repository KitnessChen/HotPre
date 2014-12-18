#!/usr/bin/env python
# coding=utf-8

import json
import os
import sys
import time

from tornado.options import options
from TwitterSearch import *


class SearchTopicDAO(object):
    def __init__(self, keyword, time):
        self.keyword = keyword
        self.time = time

    @classmethod
    def search(self):
        cur_time = time.localtime(self.time)
        finalfile = str(cur_time.tm_mon) + "_" + str(cur_time.tm_mday) + "_" + str(cur_time.tm_hour - 8)
        if os.path.isfile(os.path.join(options.finaldata_path, self.keyword) + finalfile):
            return False
        try:
            directory = os.path.join(options.rowdata_path, self.keyword)
            if not os.path.exists(directory):
                os.makedirs(directory)
            f = open(directory + '%s.txt' % str(self.time), "w")
            tso = TwitterSearchOrder() # create a TwitterSearchOrder object
            tso.set_keywords(s) # let's define all words we would like to have a look for

            # it's about time to create TwitterSearch object again
            ts = TwitterSearch(
                consumer_key = 'FNFUhV29d2QYdKAUsymGI7q9e',
                consumer_secret = 'A8bsZwcwZL8P7R6euf6sFGGrHzOxfCmrkpjh1prCDBdwKZ46Po',
                access_token = '2918540113-vuYDS9I9k792vsTNvvtVNFHMLv5o0hrGeyBaKXf',
                access_token_secret = 'vtaFxGSkxfVBJLDk8mCnjvPTlzJwIkJ67fQ5Eb0179GuT'
            )

            # start asking Twitter about the timeline
            for tweet in ts.search_tweets_iterable(tso):
                l = json.dumps([tweet['user']['screen_name'],tweet['created_at'],
                    tweet['text'],tweet['favorite_count'],tweet['retweet_count'],
                    tweet['user']['favourites_count'], tweet['user']['followers_count'],
                    tweet['user']['friends_count'], tweet['user']['listed_count']])
                f.write(l + '\n')

        except TwitterSearchException as e: # catch all those ugly errors
            print(e)
