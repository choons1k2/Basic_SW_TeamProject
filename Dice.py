import os
import random

#Dice class: 5개 주사위 던지고 다시 던질 주사위를 고르는 method
class Dice:

    #5개 주사위를 던지는 method
    @staticmethod
    def throwDice(self, diceList):
        for i in range(5):
            number = random.randrange(1, 7)
            diceList.append(number)
            print(f'{i+1}번째 주사위의 눈은 {number}입니다')

            os.system('pause')
            os.system('cls')

        print(f'결과: {diceList}')
        print('\n')
        return diceList

    #다시 던질 주사위를 고르는 method
    @staticmethod
    def chooseDice(self, diceList):
        throwAgain = input("몇번째 주사위를 다시 던질까요? (띄어쓰기로 구분): ")
        throwAgain = list(map(int, throwAgain.split()))

        for i in throwAgain:
            diceList[i+1] = random.randrange(1, 7)

        print(f'결과: {diceList}')
        print('\n')

        return diceList

