from abc import *

class Section(metaclass=ABCMeta):
    @abstractmethod
    def getScore(self, scoretype):
        pass


    @abstractmethod
    def findMax(self):
        pass

