from abc import *

class UpperSection(metaclass=ABCMeta):
    @abstractmethod
    def getScore(self, scoretype):
        pass


    @abstractmethod
    def findMax(self):
        pass

