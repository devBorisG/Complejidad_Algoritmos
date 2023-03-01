def main():
    """Create the Game Board with a function and print an integer that solve de problem
    """
    gameBoard = createGameBoard()  # (2n^3 + 68n^2 + 99n + 4) OE    #
    print(theBestWay(gameBoard))   # (21n + 8) OE                   # TOTAL DEFINITIVO: (2n^3 + 68n^2 + 120n + 12) OE => Complejidad cubica O(n^3)

def createGameBoard():
    """Do the Game Board with the 'n' that gives the player
    
    Returns:
        array: returns a function that insed it contains an array with the game board filled correctly
    """
    condition = True                                        # 1 OE                                                                   #
    while condition == True:                                # n OE                         #                                         #
        n = int(input())                                        # 3 OE                     #                                         #
        if 2 <= n <= 100:                                       # 2 OE                     #  (n(3+2(1+1+n^2))) OE  =>  2n^3+7n      #
            condition = False                                       # 1 OE                 #                                         #
            gameBoard = [list(range(n)) for _ in range(n)]          # 1(1(1) + n^2) OE     #                                         #
    return fillGameBoard(n,gameBoard)                       # (68n^2 + 92n + 2) OE                                                   # TOTAL: (2n^3 + 68n^2 + 99n + 3) OE

def fillGameBoard(n,gameBoard):
    """The player sets each row of characters and this functions evaluates if
    it has the correct legth, characters allowed and if the first entry starts with '.'

    Args:
        n (int): Contains the number entered by the player
        gameBoard (array): Contains empty but structured Game Board 

    Returns:
        array: Returns the Game Board filled with the player's specifications
    """
    firstEntry = True                                               # 1 OE                                                                                                                           #
    for i in range(n):                                              # n OE                                                                                                      #                    #      
        condition = True                                                # 1 OE                                                                                  #               #                    #
        while condition == True:                                        # n OE                                                                                  #               #                    #
            row = str(input())                                              # 3 OE                                                      #                       #               #                    #         
            if firstEntry == True and row[0] != '.':                        # 4 OE                                                      #                       #               #                    #
                    continue                                        
            elif len(row) == n and evaluateCorrectCharacters(row):          # 3 OE + (11n + 13) OE          #                           #                       #               #                    #
                condition = False                                               # 1 OE              #       #                           #                       #               #                    #
                firstEntry = False                                              # 1 OE              # 2 OE  #   6 OE + (66n + 78) OE    # 13 OE + (66n + 78) OE #               #                    #
        else:                                                               
            for j in range(n):                                          # n OE                                                                                  #               #                    #
                gameBoard[i][j] = row[j]                                    # 2 OE                                                      # 2n OE                 # (68n + 92) OE # (68n^2 + 92n) OE   # TOTAL: (68n^2 + 92n + 2) OE 
    return gameBoard                                                # 1 OE

def evaluateCorrectCharacters(value):
    """Evaluate that the player's entries contain the allowed characters

    Args:
        value (str): Contains the row of characters entered by the player that can be part of the Game Board

    Returns:
        bool: Give the answer to the evaluation, being 'False' that it does not belong to the allowed characters and
        'True' that it does belong to them
    """
    condition = True                                                                                    # 1 OE                                      #
    for i in range(len(value)):                                                                         # (n + 1) OE    #                           #
        if condition and value[i] != '.' and value[i] != 'A' and value[i] != 'o': condition = False         # 11 OE     #  (n + 1) * 11 => 11n + 11 # 
    return condition                                                                                    # 1 OE                                      # TOTAL: (11n + 13) OE

def theBestWay(gameBoard):
    """analyzes the best result the player can obtain by going through the array and getting as many
    points as possible before encountering a ghost

    Args:
        gameBoard (array): Contains the Game Board already filled with the data provided by the player

    Returns:
        int: Returns the number of the maximum amount of meal pacman can have
    """
    count = 0                               # 1 OE                                                  #
    aux = 0                                 # 1 OE                                                  #
    item = ''                               # 1 OE                                                  #
    n = len(gameBoard[0])                   # 3 OE                                                  #
    for i in range(n):                      # n OE                                                  #
        for j in range(n):                      # n OE                                  #           #
            if (i+1)%2!=0:                          # 3 OE                    #         #           #
                item = gameBoard[i][j]                  # 2 OE                #         #           #
            else:                                                       
                item = gameBoard[i][n-1-j]              # 4 OE      # 6 OE    #         #           #
            if item == 'A':                         # 1 OE                    #         #           #
                if aux < count:                         # 1 OE                #         #           #
                    aux = count                             # 1 OE  # 2 OE    #         #           #
                count = 0                               # 1 OE                #         #           #
            elif item == 'o':                       # 1 OE                    #         #           #
                count += 1                              # 1 OE      # 1 OE    # 21 OE   # 21n OE    #
    if aux < count:                         # 1 OE                                      #           #
        aux = count                             # 1 OE                                  # 1 OE      # TOTAL: (21n + 8) OE
    return aux                              # 1 OE                                                  #

if __name__ == "__main__":
    main()