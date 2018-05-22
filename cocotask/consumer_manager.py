from multiprocessing import Pool
from .rmq_consumer import CocoRMQConsumer
from .kafka_consumer import CocoKafkaConsumer
import logging
logger = logging.getLogger(__name__)

# this is aka mixture of a consumer factory and threadpool
class CocoConsumerManager(object):

    CONSUMER_CLASS = {
        "RMQ": CocoRMQConsumer,
        "KAFKA": CocoKafkaConsumer
    }

    def __init__(self, config, worker_class, pool_size, customized_logger = None):
        self._worker_class = worker_class
        self._pool = None
        self._pool_size = pool_size
        self._config = config
        if customized_logger:
            logger = customized_logger

    def start(self):
        print('0')

        self._pool = Pool()
        results = [self._pool.apply_async(CocoConsumerManager._start_consumer, args=[x, self._worker_class, self._config]) for x in range(self._pool_size)]
        self._pool.close()
        self._pool.join()

    @staticmethod
    def _start_consumer(seq, worker_class, config):
        try:
            logger.info('start consumer')
            worker = worker_class(config, seq)

            consumer_type = config["MQ_TYPE"]
            logger.info('cusumer type: {}'.format(consumer_type))
            consumer_class = CocoConsumerManager.CONSUMER_CLASS[consumer_type]

            sub_config = config[consumer_type]
            consumer = consumer_class(sub_config, worker, logger)
            consumer.connect()

        except Exception as error:
            logger.error(error)


