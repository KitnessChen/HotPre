#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from dateutil.parser import parse

import json
import os
import time

from tornado.options import options


class DataManageDAO(object):

    DATA_TYPES = [
    'twitters',
    'content_len',
    'favorites',
    'retweets',
    'user_favourites',
    'user_lists',
    'user_friends',
    'user_followers'
    ]

    FEATURES = {
    'twitters': 0,
    'favorites': 0,
    'retweets': 0,
    'user_favourites': 1,
    'user_lists': 1,
    'user_friends': 1,
    'user_followers': 1
    }

    def __init__(self, keyword, time):
        self.cur_time = time
        self.keyword = keyword
        self.data_list = []
        self.user_dict = {}

    def data_format(self):
        """
        format row data from twitter_search results
        """
        directory = os.path.join(options.rowdata_path, self.keyword)
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + '/' + str(self.cur_time.tm_mon) + "_" + str(self.cur_time.tm_mday) + "_" + str(self.cur_time.tm_hour) + '.txt'
        content = open(filename, "r")
        if not content:
            return None
        for line in content:
            try:
                data = json.loads(line)
            except:
                continue
            length = len(data[2])
            if data[0] in self.user_dict and data[1] in self.user_dict[data[0]]:
                    continue
            self.data_list.append([data[1], length, data[3], data[4], data[5], data[6], data[7], data[8]])
            if data[0] not in self.user_dict:
                self.user_dict[data[0]] = [data[1]]
            else:
                self.user_dict[data[0]].append(data[1])
        return True

    def data_collect(self):
        """
        generate format_data (/hour)
        """
        data_dict = {}
        final_list = []
        final_dict = {}
        for data in self.data_list:
            t = parse(data[0])
            time_str = datetime(t.year, t.month, t.day, t.hour).isoformat(" ")
            if time_str not in data_dict:
                data_dict[time_str] = {feature: 0 for feature in DataManageDAO.DATA_TYPES}
            hour_data = data_dict[time_str]
            for i, feature in enumerate(DataManageDAO.DATA_TYPES):
                if feature == 'twitters':
                    hour_data[feature] += 1
                else:
                    hour_data[feature] += data[i]

        directory = os.path.join(options.finaldata_path, self.keyword)
        if not os.path.exists(directory):
            os.makedirs(directory)

        for _type in DataManageDAO.DATA_TYPES:
            temp_dict = {'name': _type, "data": {}}
            for hour in data_dict:
                if _type != 'twitters':
                    temp_dict['data'][hour] = data_dict[hour][_type] / data_dict[hour]['twitters']
                else:
                    temp_dict['data'][hour] = data_dict[hour][_type]
            final_list.append(temp_dict)
            temp = 0
            for hour in data_dict:
                temp += data_dict[hour][_type]
            final_dict[_type] = temp
        final_dict['chart'] = final_list

        filename = directory + '/' + str(self.cur_time.tm_mon) + "_" + str(self.cur_time.tm_mday) + "_" + str(self.cur_time.tm_hour) + '.txt'
        outfile = open(filename, "w")
        json.dump(final_dict, outfile)

        return final_dict

    def data_manage(self):
        if self.data_format():
            return self.data_collect()
        return None

    @classmethod
    def get_features(self):
        return DataManageDAO.FEATURES


class DataCollectDAO(object):
    def __init__(self, keyword, time):
        self.time = time
        self.keyword = keyword

    def data_collect(self):
        """
        collect data from file
        """
        cur_time = time.localtime()
        directory = os.path.join(options.finaldata_path, self.keyword)
        filename = directory + "/%d_%d_%d.txt" % (cur_time.tm_mon, cur_time.tm_mday, cur_time.tm_hour)
        if not os.path.isfile(filename):
            return None
        data_file = open(filename, "r")
        return json.load(data_file)


class SampleDAO(object):

    SAMPLES = [
    'Google',
    'Billboard',
    'NiceDay',
    'TaylorSwift',
    'China',
    'HappyYulyulkDay',
    'NCTL2014'
    ]

    FEATURES = {
    'twitters': 0,
    'favorites': 0,
    'retweets': 0,
    'user_favourites': 1,
    'user_lists': 1,
    'user_friends': 1,
    'user_followers': 1
    }

    @classmethod
    def get_sample(self, keyword):
        """
        get sample data from file
        """
        filename = options.sample_path + "/%s.txt" % keyword
        if not os.path.isfile(filename):
            return None
        data_file = open(filename, "r")
        return json.load(data_file)

    @classmethod
    def get_samples(self):
        """
        get sample keywords
        """
        return SampleDAO.SAMPLES

    @classmethod
    def get_features(self):
        """
        get sample features
        """
        return SampleDAO.FEATURES