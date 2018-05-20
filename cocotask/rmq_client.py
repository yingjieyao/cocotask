# -*- coding: utf-8 -*-

import pika
import json
import logging

default_logger = logging.getLogger(__name__)

class RMQClient(object):

    def __init__(self, conf, callback = None, logger = default_logger):
        self._exchange_name = conf['EXCHANGE_NAME']
        self._queue_name = conf['QUEUE_NAME']
        self._exchange_type = conf['EXCHANGE_TYPE']
        self._setting = conf
        self._callback = callback
        self._connection = None
        self._logger = default_logger

    def connect(self, callback = None):
        self._logger.debug('start connect')
        credentials = pika.PlainCredentials(self._setting['USERNAME'], self._setting['PASSWORD'])
        parameters = pika.ConnectionParameters(self._setting['SERVER_ADDRESS'],
                                               self._setting['SERVER_PORT'],
                                               '/',
                                               credentials)
        self._connection = pika.BlockingConnection(parameters)

        channel = self._connection.channel()
        channel.exchange_declare(exchange = self._exchange_name,
                                 exchange_type = self._exchange_type)

        result = channel.queue_declare(queue = self._queue_name, durable=True)
        name = result.method.queue
        channel.queue_bind(exchange = self._exchange_name,
                           queue = result.method.queue)

        if self._callback == None:
            return

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(self.on_message,
                              queue=self._queue_name)

        channel.start_consuming()

    def on_message(self, ch, method, properties, body):
        self._callback(body)
        ch.basic_ack(delivery_tag = method.delivery_tag)