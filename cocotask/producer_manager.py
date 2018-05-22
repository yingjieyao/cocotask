from .rmq_producer import CocoRMQProducer
from .kafka_producer import CocoKafkaProducer
import logging
default_logger = logging.getLogger(__name__)

class CocoProducerManager(object):

    CONSUMER_CLASS = {
        "RMQ": CocoRMQProducer,
        "KAFKA": CocoKafkaProducer
    }

    @staticmethod
    def create_instance(config, logger = default_logger):
        producer_type = config["MQ_TYPE"]
        producer_class = CocoProducerManager.CONSUMER_CLASS[producer_type]

        sub_config = config[producer_type]
        producer = producer_class(sub_config, logger)
        return producer
