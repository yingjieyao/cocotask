# -*- coding: utf-8 -*-
from cocotask import CocoConsumerManager as CCManager
from cocotask import CocoBaseWorker
import time

from jsmin import jsmin
import json

class TestWorker(CocoBaseWorker):
    def process(self, body):
        arr = []
        for i in range(1,1000*1000*100):
            arr.append(i)
        time.sleep(10)
        print("done")

with open('config.json', 'r') as f:
    config = json.loads(jsmin(f.read()))

manager = CCManager(config, TestWorker, 1)
manager.start()

