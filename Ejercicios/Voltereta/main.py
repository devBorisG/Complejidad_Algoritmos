import numpy as np

def main():
    """
    The main function will collect the necessary data such as the length of the array and the number of flips you want to give it.
    It will then create a square array of the length entered by the user, with random numbers in it
    and it will keep flipping the array as long as the user wants it to flip.
    """
    condition = 1
    lenMat = int(input("Enter the matrix length: "))
    matrix = np.random.randint(0,100,size=(lenMat,lenMat))
    print("The following matrix was created: \n",matrix)
    while condition == 1:
        numSomSault = int(input("Enter the number of somersaults the matrix will make: "))
        matrix = turnMatrix(matrix,numSomSault)
        condition = int(input("Do you want to keep doing somersaults?\n1. Yes\n2.No\nAnswer: "))
    print("Thnx for playing :)")

def turnMatrix(matrix,numSomSault):
    """This function is in charge of turning the matrix as many times as desired (clockwise), taking the first row and turning it to the last column,
    and so on until the last row is reached. This process is repeated until the user has made all the turns desired.
    The matrix is redefined each time it is flipped to print the value and to be able to continue flipping it correctly as long as the user wishes.

    Args:
        matrix (array): Here is the matrix previously designed with the values already contained in it in order to be able to give them the turns
        numSomSault (int): Number of somersaults the matrix will make

    Returns:
        array: Returns the modified matrix after all the flips entered by the user have been given
    """
    lenMatrix = len(matrix[0])
    while numSomSault != 0:
        tempMatrix = np.zeros((lenMatrix,lenMatrix),int)
        for x in range(lenMatrix):
            tempMatrix[:,lenMatrix-1-x] = [item for item in matrix[x]]
        matrix = tempMatrix
        print("Movement",numSomSault,"\n",matrix)
        numSomSault -=1
    return matrix

if __name__ == "__main__":
    main()