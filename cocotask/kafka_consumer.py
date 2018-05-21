from .mq_consumer import CocoMQConsumer
from kafka import KafkaConsumer
import logging
default_logger = logging.getLogger(__name__)

class CocoKafkaConsumer(CocoMQConsumer):
    def __init__(self, conf, user_consumer, logger = default_logger):
    	super().__init__(conf, callback, logger)
    	self._consumer = None
        
    def connect(self):
        self._consumer = KafkaConsumer(bootstrap_servers=self._config['BOOTSTRAP_SERVERS'],
	         						   group_id=self._config['GROUP_ID'],
                                       consumer_timeout_ms=1000)

        self._consumer.subscribe(self._config['TOPIC'])

        while True:
            for message in self._consumer:
            	try:
	            	self._user_consumer.callback(message)
            	except:
            		logging.error(e)
