from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass


class C1(AbstractClassExample):
    def __init__(self, value):
        self.v1 = value
        super().__init__(value)


    def do_something(self):
        return self.value + self.v1



c = C1(12)

v = c.do_something()
print(v)
