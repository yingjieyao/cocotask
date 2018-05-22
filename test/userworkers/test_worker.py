from cocotask import CocoBaseWorker
import time

class TestWorker(CocoBaseWorker):

    def process(self, body):
        print(self._config["MQ_TYPE"])
        print("Test Action: [%d] Received %r" % (self._seq, body))
        time.sleep(5)
        print("Test Action: [%d] Done" % self._seq)
        
