from abc import abstractmethod, ABCMeta

class abstract(metaclass = ABCMeta):

    @abstractmethod
    def throwDice(self):
        pass
