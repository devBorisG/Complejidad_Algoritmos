##orange
#PREGUNTAR SI LA RESTRICCION DE SALIDA DEL USUARIO ES JUSTO CUANDO ACABE EL JUEGO O SI PUEDE SALIRSE SIN SIQUIERA COMENZAR
##

##TIEMPO 4 HORAS

import numpy as np

def main():
    play = 1
    while play == 1:
        gameBoard = createGameBoard()
        print(theBestWay(gameBoard))
        play =int(input("Do you want to continue playing?\n1.Yes\n2.No"))

def createGameBoard():
    condition = True
    while condition == True:
        n = int(input())
        if 2 <= n <= 100:
            condition = False
            gameBoard = np.empty((n,n),str)
        else:
            print("Please, make sure your input is between 2 and 100.")
    return fillGameBoard(n,gameBoard)

def fillGameBoard(n,gameBoard):
    firstEntry = True
    for i in range(n):
        correctCharacter = True
        condition = True
        while condition == True:
            row = str(input())
            if firstEntry == True and row[0] != '.':
                    print("Please verify that your first character is '.'.")
            else:
                if len(row) == n:
                    correctCharacter = evaluateCorrectCharacters(row)
                    if correctCharacter == False:
                        print("Please enter the correct charactes: '.' or 'A' or 'o',")
                    else:
                        condition = False
                        firstEntry = False
                else:
                    print("Please verify your entry, you bust be",n,"characters.")
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