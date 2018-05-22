# -*- coding: utf-8 -*-
from cocotask import CocoProducerManager as pm
import json

with open('config.json', 'r') as f:
	config = json.load(f)

producer = pm.create_instance(config)

producer.connect()
producer.send(b'aaaa44444')
producer.close()
