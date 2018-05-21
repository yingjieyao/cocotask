from abc import ABC, abstractmethod
import logging
default_logger = logging.getLogger(__name__)

class CocoUserConsumer(ABC):
    def __init__(self, conf, seq, logger = default_logger):
        super().__init__()
        self._config = conf
        self._seq = seq
        self._logger = logger


    @abstractmethod
    def callback(self):
        pass
