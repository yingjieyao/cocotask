from abc import ABC, abstractmethod
import logging
default_logger = logging.getLogger(__name__)

class CocoMQConsumer(ABC):
    def __init__(self, conf, user_consumer, logger = default_logger):
        self._config = conf
        self._user_consumer = user_consumer
        self._logger = logger
        super().__init__()

    @abstractmethod
    def connect(self):
        pass
