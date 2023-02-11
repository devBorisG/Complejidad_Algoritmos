import numpy as np

def main():
    """Create the Game Board with a function and print an integer that solve de problem
    """
    gameBoard = createGameBoard()
    print(theBestWay(gameBoard))

def createGameBoard():
    """Do the Game Board with the 'n' that gives the player
    
    Returns:
        array: returns a function that insed it contains an array with the game board filled correctly
    """
    condition = True
    while condition == True:
        n = int(input())
        if 2 <= n <= 100:
            condition = False
            gameBoard = np.empty((n,n),str)
    return fillGameBoard(n,gameBoard)

def fillGameBoard(n,gameBoard):
    """The player sets each row of characters and this functions evaluates if
    it has the correct legth, characters allowed and if the first entry starts with '.'

    Args:
        n (int): Contains the number entered by the player
        gameBoard (array): Contains empty but structured Game Board 

    Returns:
        array: Returns the Game Board filled with the player's specifications
    """
    firstEntry = True
    for i in range(n):
        condition = True
        while condition == True:
            row = str(input())
            if firstEntry == True and row[0] != '.':
                    continue
            elif len(row) == n and evaluateCorrectCharacters(row):
                condition = False
                firstEntry = False
        else:
            for j in range(n):
                gameBoard[i][j] = row[j]
    return gameBoard

def evaluateCorrectCharacters(value):
    """Evaluate that the player's entries contain the allowed characters

    Args:
        value (str): Contains the row of characters entered by the player that can be part of the Game Board

    Returns:
        bool: Give the answer to the evaluation, being 'False' that it does not belong to the allowed characters and
        'True' that it does belong to them
    """
    condition = True
    for i in range(len(value)):
        if condition and value[i] != '.' and value[i] != 'A' and value[i] != 'o': condition = False
    return condition

def theBestWay(gameBoard):
    """analyzes the best result the player can obtain by going through the array and getting as many
    points as possible before encountering a ghost

    Args:
        gameBoard (array): Contains the Game Board already filled with the data provided by the player

    Returns:
        int: Returns the number of the maximum amount of meal pacman can have
    """
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