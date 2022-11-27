from enum import Enum

class TopScore(Enum):
    Ace = 1
    Twos = 2        #해당하는 주사위 눈 *  주사위 갯수이므로, enum 사용
    Threes = 3
    Fours = 4
    Fives = 5
    Sixes = 6


from upper import UpperSection

class UpperScores(UpperSection):
    maxScore = 0

    def __init__(self, resultList, score=0):
        self.resultList = resultList


    #해당하는 주사위 눈 *  주사위 갯수이므로, enum 사용
    def getScore(self, scoretype):

        return sum([v for v in self.resultList if v == scoretype])

    def findMax(self):
        if self.score > 1:
            if self.score > super().maxScore:
                super().maxScore = self.score




#다형성: polymorphism: getScore에 어떤 TopScore이 들어가느냐에 따라 함수가 다르게 동작함

class Ace(UpperScores):


    def __init__(self, resultList, score=0):
        super().__init__(resultList)
        self.score = self.getScore(TopScore.Ace)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Ace'족보로 {self.score}점 획득하셨습니다!\n")


class Two(UpperScores):

    def __init__(self, resultList, score=0):
        super().__init__(resultList)
        self.score = self.getScore(TopScore.Twos)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Two'족보로 {self.score}점 획득하셨습니다!\n")


class Three(UpperScores):

    def __init__(self, resultList, score=0):
        super().__init__(resultList)
        self.score = self.getScore(TopScore.Threes)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Three'족보로 {self.score}점 획득하셨습니다!\n")


class Four(UpperScores):

    def __init__(self, resultList, score=0):
        super().__init__(resultList)
        self.score = self.getScore(TopScore.Fours)

        def findMax(self):
            super().findMax()
            if self.score > 1:
                print(f"축하합니다! 'Four'족보로 {self.score}점 획득하셨습니다!\n")


class Five(UpperScores):

    def __init__(self, resultList, score=0):
        super().__init__(resultList)
        self.score = self.getScore(TopScore.Fives)


    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Five'족보로 {self.score}점 획득하셨습니다!\n")


class Six(UpperScores):

    def __init__(self, resultList, score=0):
        super().__init__(resultList)
        self.score = self.getScore(TopScore.Sixes)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Six'족보로 {self.score}점 획득하셨습니다!\n")


