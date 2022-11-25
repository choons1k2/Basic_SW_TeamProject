# 박태우

from upper import UpperSection

class UpperScores(UpperSection):

    def __init__(self,resultList):
        self.resultList = resultList

    # 족보에 일치하는 주사위 개수
    def countDice(self,count,num):
        self.count = count
        self.num = num
        for i in self.resultList:
            if i == num:
                self.count +=1
        return self.count 

    # 족보의 점수 
    def score(self,num):
        self.num = num
        return self.count*num

## 아래는 족보별
# 원래는 각각 스크립트 파일로 모듈화 했었는데
# 폴더 import 하는 방식할지 말지 의논 필요?
# 동일한 내용 족보별 스크립트 파일 만들어 놓았습니다

class Ace(UpperScores):

    def __init__(self,resultList):
        super().__init__(resultList)

    def congrats(self):
        print(f' Ace 족보로 {self.score(1)}점 획득!!')


class Two(UpperScores):

    def __init__(self,resultList):
        super().__init__(resultList)

    def congrats(self):
        print(f' Two 족보로 {self.score(2)}점 획득!!')


class Three(UpperScores):

    def __init__(self,resultList):
        super().__init__(resultList)

    def congrats(self):
        print(f' Three 족보로 {self.score(3)}점 획득!!')


class Four(UpperScores):

    def __init__(self,resultList):
        super().__init__(resultList)

    def congrats(self):
        print(f' Four 족보로 {self.score(4)}점 획득!!')


class Five(UpperScores):

    def __init__(self,resultList):
        super().__init__(resultList)

    def congrats(self):
        print(f' Five 족보로 {self.score(5)}점 획득!!')


class Six(UpperScores):

    def __init__(self,resultList):
        super().__init__(resultList)

    def congrats(self):
        print(f' Six 족보로 {self.score(6)}점 획득!!')


