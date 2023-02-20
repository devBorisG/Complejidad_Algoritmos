import numpy as np

def voltearMatriz(matriz):
    n = len(matriz[0])
    auxMatriz = np.zeros((n,n))
    for row in len(matriz[0]):
        fila = matriz[row]
        for i in n:
            
