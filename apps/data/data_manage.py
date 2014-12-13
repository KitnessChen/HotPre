#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from dateutil.parser import parse

import json
import os
import time

from tornado.options import options


class DataManage(object):
    def __init__(self, topic, time):
        self.time = time
        self.topic = topic
        self.data_list = []
        self.user_dict = {}

    def data_format(self):
        content = open(os.path.join(options.rowdata_path, '%s/%s.txt' % (self.topic, str(self.time))), "r")
        for line in content:
            try:
                data = json.loads(line)
            except:
                continue
            # print line
            length = len(data[2])
            if data[0] in self.user_dict and data[1] in self.user_dict[data[0]]:
                    continue
            self.data_list.append([data[1], length, data[3], data[4], data[5], data[6], data[7], data[8]])
            if data[0] not in self.user_dict:
                self.user_dict[data[0]] = [data[1]]
            else:
                self.user_dict[data[0]].append(data[1])
            # print line[0]


    def data_collect(self):
        hour_data = {'twitter_count': 0, 'content_len': 0, 'favorites_count': 0, 'retweet_count': 0,
                     'user_favourites_count': 0, 'user_listed_count': 0, 'user_friends_count': 0,
                     'user_followers_count': 0}
        cur_time = time.localtime()
        for data in self.data_dict:
            time_str = data[0]
            t = parse(time_str)
            if t.day != cur_time.tm_mday or t.hour != cur_time.tm_hour - 8:
                continue
            hour_data['twitter_count'] += 1
            hour_data['content_len'] += data[1]
            hour_data['favorites_count'] += data[2]
            hour_data['retweet_count'] += data[3]
            hour_data['user_favourites_count'] += data[4]
            hour_data['user_listed_count'] += data[5]
            hour_data['user_friends_count'] += data[6]
            hour_data['user_followers_count'] += data[7]

        directory = os.path.join(options.finaldata_path, self.topic)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        filename = os.path.join(directory, str(t.tm_mon) + "_" + str(t.tm_mday) + "_" + str(cur_time.tm_hour - 8))
        outfile = open(filename, "w")
        for detail in hour_data:
            outfile.write(detail + ": " + str(hour_data[detail]) + "\n")
