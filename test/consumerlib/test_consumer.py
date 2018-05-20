from cocotask import BaseConsumer
import time

class TestConsumer(BaseConsumer):
    def callback(self, body):
        print("TestConsumer: [%d] Received %r" % (self._sequence, body))
        time.sleep(5)
        print("TestConsumer: [%d] Done" % self._sequence)
        
