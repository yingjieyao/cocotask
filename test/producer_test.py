# -*- coding: utf-8 -*-
from cocotask import CocoProducerManager as pm
from jsmin import jsmin
import json

with open('config.json', 'r') as f:
    config = json.loads(jsmin(f.read()))

producer = pm.create_instance(config)

producer.connect()
producer.send(b'aaaa44444')
producer.close()
