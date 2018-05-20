# -*- coding: utf-8 -*-

import time
from cocotask import RMQClient
import logging
default_logger = logging.getLogger(__name__)

class BaseConsumer(object):
    def __init__(self, config, seq, logger = default_logger):
        self._client = RMQClient(config, self.callback)
        self._sequence = seq
        self._logger = logger

    def start(self):
        self._logger.debug('start consumer')
        self._client.connect()


    def callback(self, body):
        self._logger.debug(" [%d] Received %r" % (self._sequence, body))
        time.sleep(5)
        self._logger.debug(" [%d] Done" % self._sequence)
