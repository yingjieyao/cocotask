from multiprocessing import Pool
import logging
default_logger = logging.getLogger(__name__)

class ConsumerManager(object):

    def __init__(self, config, consumer_class, pool_size, logger = default_logger):
        self._consumer_class_name = consumer_class
        self._pool = None
        self._pool_size = pool_size
        self._logger = logger
        self._config = config

    def start(self):
        self._pool = Pool()
        results = [self._pool.apply_async(ConsumerManager._start_consumer, args=[x, self._consumer_class_name, self._config]) for x in range(self._pool_size)]
        self._pool.close()
        self._pool.join()

    @staticmethod
    def _start_consumer(seq, class_name, config):
        print('start')
        consumer = class_name(config, seq)
        consumer.start()

