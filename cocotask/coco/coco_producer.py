#!/usr/bin/python
# -*- coding:utf-8 -*-
#############################
# File Name: coco_producer.py
# Author: yogurtyao
# Mail: yogurtyao@tencent.com
# Created Time: 2019-01-06 16:55:19
#############################


import json
import requests
from ..base_producer import CocoBaseProducer

class CocoCocoProducer(CocoBaseProducer):

    def __init__(self, conf, logger=None):
        self._headers = {'Authorization': 'Token: {}'.format(conf.get('TOKEN'))}
        self._producer_url = conf.get('PRODUCER_URL')
        super().__init__(conf, logger)


    def connect(self):
        pass

    def send(self, data):
        requests.post(self._producer_url, headers=self._headers, json={"message": data})


    def close(self):
        pass
