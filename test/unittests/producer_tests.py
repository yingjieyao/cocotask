from cocotask import CocoProducerManager as pm
import unittest

class ProducerTests(unittest.TestCase):
	def setup(self):
		pass


	def test_create_producer_with_invalid_type(self):
		config = {
			"MQ_TYPE":"AAA"
		}

		producer = pm.create_instance(config)
		self.assertIsNone(producer)


	def test_create_rmq_producer_with_invalid_config(self):
		config = {
			"MQ_TYPE":"RMQ"
		}

		producer = pm.create_instance(config)
		self.assertIsNone(producer)


	def test_create_rmq_producer_with_valid_config(self):
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

		producer = pm.create_instance(config)
		self.assertIsNotNone(producer)

	def test_create_kafka_producer_with_valid_config(self):
		config = {
			"MQ_TYPE":"KAFKA",
		    "KAFKA": {
		        "BOOTSTRAP_SERVERS": "127.0.0.1",
		        "BROKER_PORT": 9092,
		        "TOPIC": "test_topic_1",
		        "GROUP_ID": "test_consumer_group_1"
		    },
		}

		producer = pm.create_instance(config)
		self.assertIsNotNone(producer)


	def test_create_redis_producer_with_valid_config(self):
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

		producer = pm.create_instance(config)
		self.assertIsNotNone(producer)


if __name__ == '__main__':
    unittest.main()