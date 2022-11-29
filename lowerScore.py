from upper import UpperSection

class LowerScores(UpperSection):
    maxScore = 0
    
    def __init__(self,resultList,score=0):
        self.resultList = resultList

    def findMax(self):
        if self.score >1:
            if self.score>super().maxScore:
                super().maxScore = self.score

    # 재정의
    def getScore(self):
        return sum([v for v in self.resultList])

    #동일한 요소 개수 구하기
    def countTheSame(self,resultList):
        
        counter = []

        for v in self.resultList:
            counter.append(self.resultList.count(v))
        counter = set(counter)
        return counter


    # 연속된 수 구하기 
    def straight(self,resultList):
        
        straightList = []
        resultList = sorted(set(self.resultList))
        straightList = resultList
                
        return straightList
        
        




#===============================================================================            


#모든 눈의 합
class Choice(LowerScores):  

    def __init__(self,resultList,score=0):
        super().__init__(resultList)
        self.score = self.getScore()

    def findMax(self):
        super().findMax()
        if self.score>1:
            print(f"축하합니다! 'Choice'족보로 {self.score}점 획득하셨습니다!\n") 


##sample = [1,2,3,3,4]
##a = Choice(sample)
##print(a.getScore())


#================================================================

# 4개 같을 때 >> 모든 눈의 합 + 5

class FourOfaKind(LowerScores):

    def __init__(self,resultList,score=0):
        super().__init__(resultList)
        self.score = self.getScore()


    def findMax(self):
        super().findMax()
        if self.score>1:
            print(f"축하합니다! 'Four of a kind'족보로 {self.score}점 획득하셨습니다!\n") 

    def countTheSame(self,resultList):
        super().countTheSame(self.resultList)


    def getScore(self):
        if 4 in super().countTheSame(self.resultList):
            return sum([v for v in self.resultList]) + 5
        else:
            return 0

        
##sample = [2,2,2,2,3]
##a = FourOfaKind(sample)
##print(a.getScore())


#=================================================================

# 3개, 2개 같을 때 >> 모든 눈의 합 + 5

class FullHouse(LowerScores):

    def __init__(self,resultList,score=0):
        super().__init__(resultList)
        self.score = self.getScore()


    def findMax(self):
        super().findMax()
        if self.score>1:
            print(f"축하합니다! 'Full House'족보로 {self.score}점 획득하셨습니다!\n") 

    def countTheSame(self,resultList):
        super().countTheSame(self.resultList)


    def getScore(self):
        if 3 in super().countTheSame(self.resultList) and 2 in super().countTheSame(self.resultList):
            return sum([v for v in self.resultList]) + 5
        
        else:
            return 0

##sample = [1,2,2,1,1]
##a = FullHouse(sample)
##print(a.getScore())


#=================================================================


# 연속된 3개의 수 , 15점
# 4개가 연속되어도 SmallStraight 가능, Largestraight가 가능 하면 어차피 maxScore

class SmallStraight(LowerScores):

    def __init__(self,resultList,score=0):
        super().__init__(resultList)
        self.score = self.getScore()

    def findMax(self):
        super().findMax()
        if self.score>1:
            print(f"축하합니다! 'Small Straight'족보로 {self.score}점 획득하셨습니다!\n") 

    def getScore(self):
        straightList = super().straight(self.resultList)
        if len(straightList) >= 3:
           for i in range(len(straightList)-2):
               if straightList[i] == straightList[i+1]-1 and straightList[i+1] == straightList[i+2] - 1:
                   return 15
                   continue
           return 0        
        else:
            return 0
        

                    
            
##sample = [1,2,1,4,5]
##sample2 = [2,1,6,4,5]
##
##a = SmallStraight(sample)
##b = SmallStraight(sample2)
##
##print(a.straight(sample))
##print(b.straight(sample2))
##
##print(a.getScore())
##print(b.getScore())



#================================================================

#연속된 4개의 수 , 30점
    
class LargeStraight(LowerScores):

    def __init__(self,resultList,score=0):
        super().__init__(resultList)
        self.score = self.getScore()

    def findMax(self):
        super().findMax()
        if self.score>1:
            print(f"축하합니다! 'Large Straight'족보로 {self.score}점 획득하셨습니다!\n") 

    def getScore(self):
        straightList = super().straight(self.resultList)
        if len(straightList) >= 4:
           for i in range(len(straightList)-2):
               if straightList[i] == straightList[i+1]-1 and straightList[i+1] == straightList[i+2] - 1 and straightList[i+2] == straightList[i+3] -1:
                   return 30
               else:
                   return 0
        else:
            return 0


##sample = [1,2,6,4,5]
##sample2 = [4,2,3,2,5]
##
##a = LargeStraight(sample)
##b = LargeStraight(sample2)
##
##print(a.straight(sample))
##print(b.straight(sample2))
##print(a.getScore())
##print(b.getScore())

# =================================================================

# 전부 같은 숫자 (5개) , 50점
class Yacht(LowerScores):

    def __init__(self,resultList,score=0):
        super().__init__(resultList)
        self.score = self.getScore()


    def findMax(self):
        super().findMax()
        if self.score>1:
            print(f"축하합니다! 'Yacht'족보로 {self.score}점 획득하셨습니다!\n") 

    def countTheSame(self,resultList):
        super().countTheSame(self.resultList)


    def getScore(self):
        if 5 in super().countTheSame(self.resultList):
            return 50
        else:
            return 0
        

##sample = [1,1,1,1,1]
##a = Yacht(sample)
##print(a.getScore())
