# -*- coding: utf-8 -*-
from cocotask import RMQProducer
import json

with open('config.json', 'r') as f:
	config = json.load(f)

producer = RMQProducer(config)

producer.connect()
producer.send('aaaa11111')
producer.close()
