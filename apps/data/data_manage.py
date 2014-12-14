#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from dateutil.parser import parse

import json
import os
import time

from tornado.options import options


class DataManageDAO(object):
    def __init__(self, topic, time):
        self.time = time
        self.topic = topic
        self.data_list = []
        self.user_dict = {}

    @classmethod
    def data_format(self):
        directory = os.path.join(options.rowdata_path, self.topic)
        if not os.path.exists(directory):
            os.makedirs(directory)
        content = open(directory + '%s.txt' % str(self.time), "r")
        if not content:
            return None
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
        return True

    @classmethod
    def data_collect(self):
        final_data = []
        cur_time = time.localtime(self.time)
        for data in self.data_dict:
            t = parse(data[0])
            time_str = datetime(t.year, t.month, t.day, t.hour).isoformat(" ")
            if time_str not in final_data:
                final_data[time_str] = {'twitter_count': 0, 'content_len': 0, 'favorites_count': 0,
                                        'retweet_count': 0, 'user_favourites_count': 0, 'user_listed_count': 0,
                                        'user_friends_count': 0, 'user_followers_count': 0}
            hour_data = final_data[time_str]
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
        # data format!!!!
        filename = directory + str(cur_time.tm_mon) + "_" + str(cur_time.tm_mday) + "_" + str(cur_time.tm_hour)
        outfile = open(filename, "w")
        json.dump(final_data, outfile)

        return final_data

    @classmethod
    def data_manage(self):
        if self.data_format():
            return self.data_collect()
        return None


class DataCollectDAO(object):
    def __init__(self, topic, time):
        self.time = time
        self.topic = topic

    @classmethod
    def data_collect(self):
        cur_time = time.localtime()
        directory = os.path.join(options.finaldata_path, self.topic)
        filename = directory + "/%d_%d_%d.txt" % (cur_time.tm_mon, cur_time.tm_mday, cur_time.tm_hour - 8)
        if not os.path.isfile(filename):
            return None
        data_file = open(filename, "r")
        return json.load(data_file)


class SampleDAO(object):
    def __init__(self, topic):
        self.topic = self.topic

    @classmethod
    def get_sample(self):
        filename = options.sample_path + "/%s.txt" % self.topic
        if not os.path.isfile(filename):
            return None
        data_file = open(filename, "r")
        return json.load(data_file)

    @classmethod
    def get_samples(self):
        samples = ['Google', 'Billboard', 'NiceDay', 'TaylorSwift', 'China', 'HappyYulyulkDay', 'NCTL2014']
        return samples
