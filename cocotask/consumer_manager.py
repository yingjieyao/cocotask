from multiprocessing import Pool
from .rmq_consumer import CocoRMQConsumer
from .kafka_consumer import CocoKafkaConsumer
import logging
default_logger = logging.getLogger(__name__)

# this is aka mixture of a consumer factory and threadpool
class CocoConsumerManager(object):

    CONSUMER_CLASS = {
        "RMQ": CocoRMQConsumer,
        "KAFKA": CocoKafkaConsumer
    }

    def __init__(self, config, consumer_class, pool_size, logger = default_logger):
        self._consumer_class_name = consumer_class
        self._pool = None
        self._pool_size = pool_size
        self._logger = logger
        self._config = config

    def start(self):
        self._pool = Pool()
        results = [self._pool.apply_async(CocoConsumerManager._start_consumer, args=[x, self._consumer_class_name, self._config, self._logger]) for x in range(self._pool_size)]
        self._pool.close()
        self._pool.join()

    @staticmethod
    def _start_consumer(seq, user_class_name, config, logger):
        print('start')
        try:
            user_consumer = user_class_name(config, seq)

            mq_customer_type_name = config["MQ_TYPE"]
            mq_customer_class_name = CocoConsumerManager.CONSUMER_CLASS[mq_customer_type_name]

            sub_config = config[mq_customer_type_name]
            consumer = mq_customer_class_name(sub_config, user_consumer, logger)
            consumer.connect()

        except Exception as error:
            logging.error(error)


