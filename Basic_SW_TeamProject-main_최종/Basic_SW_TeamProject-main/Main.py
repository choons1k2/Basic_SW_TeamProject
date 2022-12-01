from Dice import Dice
import upperScore
import lowerScore
import os
import sys

#모든 판의 점수의 합
score1 = 0
score2 = 0

if(input('게임을 시작하려면 아무거나, 프로그램을 종료하려면 e를 누르시오: ') == 'e'):
    sys.exit("종료")
print("\n")

#다형성: 상단항목에 만족하는 것들 중 최댓값 도출
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
    Six.findMax()


    return upperScore.maxScore

#다형성: 하단 항목에 만족하는 것들 중 최댓값 도출
def lowerMax(DiceList):
    choice = lowerScore.Choice(DiceList)
    choice.findMax()

    fourOfAkind = lowerScore.FourOfaKind(DiceList)
    fourOfAkind.findMax()

    fullhouse = lowerScore.FullHouse(DiceList)
    fullhouse.findMax()

    smallStraight = lowerScore.SmallStraight(DiceList)
    smallStraight.findMax()

    largeStraight = lowerScore.LargeStraight(DiceList)
    largeStraight.findMax()

    yacht = lowerScore.Yacht(DiceList)
    yacht.findMax()

    return lowerScore.maxScore

#상단 하단 중 total max구하는 method
def totalMax(DiceList):
    player_upperMax = upperMax(DiceList)
    print(f"상단 최고점: {player_upperMax}")

    player_lowerMax = lowerMax(DiceList)
    print(f"하단 최고점: {player_lowerMax}")

    if (player_lowerMax > player_upperMax):
        return player_lowerMax

    else:
        return player_upperMax



for i in range(8):

    print(f"{i+1}번째 판입니다.\n플레이어1 차례입니다.\n")
    #Player1의 주사위
    DiceList1 = list()
    DiceList1 = Dice.throwDice(DiceList1)

    #상하단 최고점 판단 및 비교
    player1Tmp = totalMax(DiceList1)

    #전역변수 초기화
    upperScore.maxScore=0
    lowerScore.maxScore=0

    #주사위는 2번까지 다시 던질 수 있음
    for x in range(2):
        exit = Dice.chooseDice(DiceList1)
        if exit:
            break
        else:
            player1Tmp = totalMax(DiceList1) #상하단 최고점 판단 및 비교

            #전역변수 초기화
            upperScore.maxScore=0
            lowerScore.maxScore=0
    #각 판 마다 최고점: playerTmp, score1: 모든 판의 점수의 합
    score1 = score1 + player1Tmp



    os.system('pause')
    os.system('cls')

    #Player2의 주사위
    DiceList2 = list()
    DiceList1 = Dice.throwDice(DiceList2)

    #상하단 최고점 판단 및 비교
    player2Tmp = totalMax(DiceList2)

    #전역변수 초기화
    upperScore.maxScore=0
    lowerScore.maxScore=0

    #주사위는 2번까지 다시 던질 수 있음
    for x in range(2):
        exit = Dice.chooseDice(DiceList2)
        if exit:
            #전역변수 초기화
            upperScore.maxScore=0
            lowerScore.maxScore=0

            break
        else:
            player2Tmp = totalMax(DiceList2) #상하단 최고점 판단 및 비교

            #전역변수 초기화
            upperScore.maxScore=0
            lowerScore.maxScore=0

    #각 판 마다 최고점: playerTmp, score1: 모든 판의 점수의 합
    score2 = score2 + player2Tmp







    print(f"\n{i+1}번째 판: \n누적점수: 플레이어1 - {score1}, 플레이어2 - {score2}\n")




    os.system('pause')
    os.system('cls')
