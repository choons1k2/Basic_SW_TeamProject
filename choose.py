class throwAgain:
    def chooseDice(self):
        throwAgain = input("몇번째 주사위를 다시 던질까요? (띄어쓰기로 구분): ")
        throwAgain = list(map(int, throwAgain.split()))

        return throwAgain
        
