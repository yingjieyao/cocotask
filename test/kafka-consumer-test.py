from kafka import KafkaConsumer
import time
import threading, logging, time
import multiprocessing

class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()
        
    def stop(self):
        self.stop_event.set()
        
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
        						 group_id='test2',
                                 consumer_timeout_ms=1000)
        consumer.subscribe(['test2'])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                print('{}'.format(message.value))
                time.sleep(5)
                if self.stop_event.is_set():
                    break

        consumer.close()



consumer = Consumer()
consumer.start()
