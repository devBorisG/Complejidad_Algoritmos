##TIEMPO 4 HORAS

import numpy as np

def main():
    gameBoard = createGameBoard()
    print(theBestWay(gameBoard))

def createGameBoard():
    condition = True
    while condition == True:
        n = int(input())
        if 2 <= n <= 100:
            condition = False
            gameBoard = np.empty((n,n),str)
    return fillGameBoard(n,gameBoard)

def fillGameBoard(n,gameBoard):
    firstEntry = True
    for i in range(n):
        correctCharacter = True
        condition = True
        while condition == True:
            row = str(input())
            if firstEntry == True and row[0] != '.':
                    continue
            else:
                if len(row) == n:
                    correctCharacter = evaluateCorrectCharacters(row)
                    if correctCharacter == False:
                        continue
                    else:
                        condition = False
                        firstEntry = False
        else:
            for j in range(n):
                gameBoard[i][j] = row[j]
    return gameBoard

def evaluateCorrectCharacters(value):
    condition = True
    empty = '.'
    ghost = 'A'
    meal = 'o'
    for i in range(len(value)):
        if condition == True:
            if value[i] != empty and value[i] != ghost and value[i] != meal: condition = False
            else: condition = True
    return condition

def theBestWay(gameBoard):
    count = 0
    aux = 0
    item = ''
    n = len(gameBoard[0])
    for i in range(n):
        for j in range(n):
            if (i+1)%2!=0:
                item = gameBoard[i][j]
            else:
                item = gameBoard[i][n-1-j]
            
            if item == 'A':
                if aux < count:
                    aux = count    
                count = 0
            elif item == 'o':
                count += 1
    if aux < count:
        aux = count
    return aux
            
if __name__ == "__main__":
    main()