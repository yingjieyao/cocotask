from cocotask import CocoUserConsumer
import time

class TestConsumer(CocoUserConsumer):

    def callback(self, body):
        print("TestConsumer: [%d] Received %r" % (self._seq, body))
        time.sleep(5)
        print("TestConsumer: [%d] Done" % self._seq)
        
