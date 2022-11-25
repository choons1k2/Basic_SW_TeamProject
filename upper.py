from abc import *

class UpperSection(metaclass=ABCMeta):

    @abstractmethod
    def countDice(self):
        pass

    @abstractmethod
    def score(self):
        pass    


