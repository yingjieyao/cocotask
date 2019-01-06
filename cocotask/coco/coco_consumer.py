#!/usr/bin/python
# -*- coding:utf-8 -*-
#############################
# File Name: coco_consumer.py
# Author: yogurtyao
# Mail: yogurtyao@tencent.com
# Created Time: 2019-01-06 16:55:08
#############################

import requests
import json
from ..base_consumer import CocoBaseConsumer
from multiprocessing import Process

class CocoCocoConsumer(CocoBaseConsumer):

    def __init__(self, conf, worker, logger=None):
        self._headers = {'Authorization': 'Token: {}'.format(conf.get('TOKEN'))}
        self._consumer_url = conf.get('CONSUMER_URL')
        super().__init__(conf, worker, logger)

    def connect(self):
        while True:
            resp = requests.get(self._consumer_url, headers=self._headers)
            json_data = json.loads(resp.text)
            if json_data.get('error', -1) == 0:
                self.process_data(json_data.get('result'))


    def process_data(self, data):
        worker = self._worker_class(self._config)
        p = Process(target=worker.process, args=(data, ))
        p.start()
        p.join()
