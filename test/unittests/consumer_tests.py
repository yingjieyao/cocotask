import cocotask
from cocotask import CocoConsumerManager, CocoBaseWorker
from cocotask.rabbitmq.rmq_consumer import CocoRMQConsumer
from cocotask.kafka.kafka_consumer import CocoKafkaConsumer
from cocotask.redis.redis_consumer import CocoRedisConsumer

from unittest.mock import patch
import unittest

class TestWorker(CocoBaseWorker):
    def process(self, body):
        pass


class ConsumerTests(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    @patch.object(CocoRMQConsumer, 'connect')
    def test_create_rmq_consumer_with_mock(self, mock_method):
        config = {
            "MQ_TYPE":"RMQ",
            "RMQ":{
                "SERVER_ADDRESS": "127.0.0.1",
                "SERVER_PORT": 5672,
                "VIRTUAL_HOST": "",
                "USERNAME": "guest",
                "PASSWORD": "guest",
                "EXCHANGE_NAME": "test_exchange_1",
                "QUEUE_NAME": "test_queue_1",
                "EXCHANGE_TYPE": "direct"                   
            }
        }

        manager = CocoConsumerManager(config, TestWorker, 1)
        manager._start_consumer(1, TestWorker, config)
        mock_method.assert_called_once()


    @patch.object(CocoKafkaConsumer, 'connect')
    def test_create_kafka_consumer_with_mock(self, mock_method):
        config = {
            "MQ_TYPE":"KAFKA",
            "KAFKA": {
                "BOOTSTRAP_SERVERS": "127.0.0.1",
                "BROKER_PORT": 9092,
                "TOPIC": "test_topic_1",
                "GROUP_ID": "test_consumer_group_1"
            }
        }

        manager = CocoConsumerManager(config, TestWorker, 1)
        manager._start_consumer(1, TestWorker, config)
        mock_method.assert_called_once()


    @patch.object(CocoRedisConsumer, 'connect')
    def test_create_redis_consumer_with_mock(self, mock_method):
        config = {
            "MQ_TYPE":"REDIS",
            "REDIS": {
                "SERVER": "127.0.0.1",
                "PORT": 6379,
                "DB": 7,
                "QUEUE": "trainqueue",
                "PASSWORD": "abcd1234"
            }
        }

        manager = CocoConsumerManager(config, TestWorker, 1)
        manager._start_consumer(1, TestWorker, config)
        mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()