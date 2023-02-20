import numpy as np

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

def main():
    cantVueltas = int(input("Ingrese la cantidad de volteretas que quiere que de la matriz: "))
    print(voltearMatriz(matriz,cantVueltas))

def voltearMatriz(matriz,cantVueltas):
    while cantVueltas != 0:
        n = len(matriz[0])
        auxMatriz = np.zeros((n,n),int)
        for row in range(n):
            fila = matriz[row]
            auxMatriz[:,n-1-row] = [a for a in fila]
        matriz = auxMatriz
        cantVueltas -=1
    return matriz
    
if __name__ == "__main__":
    main()