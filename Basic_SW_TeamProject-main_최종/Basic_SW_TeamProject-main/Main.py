from Dice import Dice
import upperScore
import lowerScore

import sys

if(input('게임을 시작하려면 아무거나, 프로그램을 종료하려면 e를 누르시오: ') == 'e'):
    sys.exit("종료")

#다형성
def upperMax(DiceList):
    Ace = upperScore.Ace(DiceList)
    Ace.findMax()

    Two = upperScore.Two(DiceList)
    Two.findMax()

    Three = upperScore.Three(DiceList)
    Three.findMax()

    Four = upperScore.Four(DiceList)
    Four.findMax()

    Five = upperScore.Five(DiceList)
    Five.findMax()

    Six = upperScore.Six(DiceList)
    Five.findMax()

    return upperScore.UpperScores.maxScore


def upperMax(DiceList):
    choice



score1 = 0
score2 = 0

for i in range(8):


    #Player1의 주사위
    DiceList1 = list()
    Dice.throwDice(DiceList1)
    #주사위는 2번까지 다시 던질 수 있음
    for i in range(2):
        exit = Dice.chooseDice(DiceList1)
        if exit:
            break

    upperMax = upperMax(DiceList1)
    print(f"플레이어1의 상단 최고점: {upperMax}")





    #Player2의 주사위
    DiceList2 = list()
    Dice.throwDice(DiceList2)

    #주사위는 2번까지 다시 던질 수 있음
    for i in range(2):
        exit = Dice.chooseDice(DiceList2)
        if exit:
            break


    upperMax = upperMax(DiceList1)
    print(f"플레이어2의 상단 최고점: {upperMax}")