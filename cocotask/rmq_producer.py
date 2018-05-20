# -*- coding: utf-8 -*-

import pika
import json

class RMQProducer(object):

    def __init__(self, conf):
        self._exchange_name = conf['EXCHANGE_NAME']
        self._queue_name = conf['QUEUE_NAME']
        self._exchange_type = conf['EXCHANGE_TYPE']
        self.setting = conf
        self.connection = None
        self.channel = None

    def connect(self, callback = None):
        credentials = pika.PlainCredentials(self.setting['USERNAME'], self.setting['PASSWORD'])
        parameters = pika.ConnectionParameters(self.setting['SERVER_ADDRESS'],
                                               self.setting['SERVER_PORT'],
                                               '/',
                                               credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange=self._exchange_name,
                                 exchange_type=self._exchange_type)
        self.channel.queue_declare(queue=self._queue_name, durable=True)


    def send(self, data):
      self.channel.basic_publish(exchange=self._exchange_name, 
                      routing_key=self._queue_name, 
                      body=data, 
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))

    def close(self):
        self.connection.close()


