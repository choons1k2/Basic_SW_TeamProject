from enum import Enum

maxScore = 0




from abstractSection import Section

class UpperScores(Section):


    def __init__(self, resultList, score=0):
        self.resultList = resultList



    def getScore(self, scoretype):

        self.score = sum([v for v in self.resultList if v == scoretype])

    def findMax(self):
        global maxScore
        if self.score > 1:
            if self.score > maxScore:
                maxScore = self.score




#다형성: polymorphism: getScore에 어떤 TopScore이 들어가느냐에 따라 함수가 다르게 동작함

class Ace(UpperScores):


    def __init__(self, resultList):
        super().__init__(resultList)
        super().getScore(1)

    def findMax(self):
        super().findMax()
        #족보를 만족하는 경우 무조건 메시지 출력
        if self.score > 1:
            print(f"축하합니다! 'Ace'족보로 {self.score}점 획득하셨습니다!\n")


class Two(UpperScores):


    def __init__(self, resultList):
        super().__init__(resultList)
        super().getScore(2)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Two'족보로 {self.score}점 획득하셨습니다!\n")


class Three(UpperScores):


    def __init__(self, resultList):
        super().__init__(resultList)
        super().getScore(3)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Three'족보로 {self.score}점 획득하셨습니다!\n")


class Four(UpperScores):


    def __init__(self, resultList):
        super().__init__(resultList)
        super().getScore(4)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Four'족보로 {self.score}점 획득하셨습니다!\n")


class Five(UpperScores):


    def __init__(self, resultList):
        super().__init__(resultList)
        super().getScore(5)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Five'족보로 {self.score}점 획득하셨습니다!\n")


class Six(UpperScores):


    def __init__(self, resultList):
        super().__init__(resultList)
        super().getScore(6)

    def findMax(self):
        super().findMax()
        if self.score > 1:
            print(f"축하합니다! 'Six'족보로 {self.score}점 획득하셨습니다!\n")


