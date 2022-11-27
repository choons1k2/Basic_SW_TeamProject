from Dice import Dice
import upperScore
import os
import model


while (True):
    if(input('게임을 시작하려면 아무거나, 프로그램을 종료하려면 e를 누르시오: ') == 'e'):
        break

    #Player1의 주사위
    DiceList1 = list()
    Dice.throwDice(DiceList1)
    Dice.chooseDice(DiceList1)


    #Player2의 주사위
    DiceList2 = list()
    Dice.throwDice(DiceList2)
    Dice.chooseDice(DiceList2)

