from abc import ABC, abstractmethod
import logging
from multiprocessing import Pool
default_logger = logging.getLogger(__name__)

class CocoBaseConsumer(ABC):
    def __init__(self, conf, worker_class, pool_size=4, logger = None):
        self._config = conf
        self._worker_class = worker_class
        self._logger = logger if logger else default_logger
        self._pool = Pool(pool_size)
        super().__init__()


    def __del__(self):
        self._pool.close()
        self._pool.join()


    @abstractmethod
    def connect(self):
        pass
