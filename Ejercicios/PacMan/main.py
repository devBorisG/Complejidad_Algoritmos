##red
#POSIBLES FUNCIONES
#1. Construccion de tablero (Matriz)
#2. Avanzar de izq a der o inversa (tal vez con número par o impar)
#3. Buscar conteo del mayor numero de comida posible obtenida (es decir buscar el mayor número de comida posible entre fantasmas)
#4. Verificacion de que el jugador solo ingrese un caracter por indice

#POSIBLES METODOS
#1. Condicional de pregunta si el usuario quiere seguir jugando
#2. Condicional de verificacion si la primera entrada es unicamente un espacio ( '.' ) 
#3. Condicional de que sean las entradas propuestas inicialmente por el jugador
##

##orange
#PREGUNTAR SI LA RESTRICCION DE SALIDA DEL USUARIO ES JUSTO CUANDO ACABE EL JUEGO O SI PUEDE SALIRSE SIN SIQUIERA COMENZAR
##

import numpy as np

def main():
    createGameBoard()

def createGameBoard():
    n = int(input())
    gameBoard = np.empty((n,n),str)
    fillGameBoard(n,gameBoard)

def fillGameBoard(n,gameBoard):
    for i in range(n):
        cond = False
        while cond == False:
            row = str(input())
            cond = evaluateCorrectCharacters(row)
            if cond == False:
                print("Please enter the correct charactes: '.' or 'A' or 'o'")
        else:
            for j in range(n):
                gameBoard[i][j] = row[j]

def evaluateCorrectCharacters(value):
    empty = '.'
    ghost = 'A'
    meal = 'o'
    for i in range(len(value)):
        if value[i] != empty or value[i] != ghost or value[i] != meal:
            return False

if __name__ == "__main__":
    main()