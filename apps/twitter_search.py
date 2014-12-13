#!/usr/bin/env python
# coding=utf-8

import json
import os
import sys

from tornado.options import options
from TwitterSearch import *


reload(sys)
sys.setdefaultencoding("utf-8")


class SearchTopic(object):
    def __init__(self, topic, time):
        self.topic = topic
        self.time = time

    def search(self):
        try:
            f = open(os.path.join(options.rowdata_path, '%s/%s.txt' % (self.topic, str(self.time))), "w")
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
