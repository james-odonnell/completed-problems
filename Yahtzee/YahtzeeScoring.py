import math

def yahtzee_upper(aList):
    scoreOne = 0
    scoreTwo = 0
    scoreThree = 0
    scoreFour = 0
    scoreFive = 0
    scoreSix = 0
    for position in range(len(aList)):
        if aList[position] == 1:
            scoreOne = scoreOne + 1
        elif aList[position] == 2:
            scoreTwo = scoreTwo + 2
        elif aList[position] == 3:
            scoreThree = scoreThree + 3
        elif aList[position] == 4:
            scoreFour = scoreFour + 4
        elif aList[position] == 5:
            scoreFive = scoreFive + 5
        elif aList[position] == 6:
            scoreSix = scoreSix + 6

    print(max(scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive, scoreSix))




yahtzee_upper([2, 3, 5, 5, 6])   # 10
yahtzee_upper([1, 1, 1, 1, 3])   # 4
yahtzee_upper([1, 1, 1, 3, 3])   # 6
yahtzee_upper([1, 2, 3, 4, 5])   # 5
yahtzee_upper([6, 6, 6, 6, 6])   # 30
