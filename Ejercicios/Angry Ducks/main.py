import math

"""Global variable definitions"""
g = 9.80665
pi = 3.14159


def main():
    """The main function receives the necessary data (height, place points, number of attemps, angle and initial velocity)
    and executes the function for the number of times (n) entered.
    
    It was necessary the use of an infinite loop and the use of a try cacth containing the exception EOFError to execute 
    the program as many times as necessary until the program does not receive any more inputs, in order to receive the 
    acceptance of the code in the beecrowd platform. 
    """
    while True:
        try:
            h = float(input())
            points_nlogony = input().split(sep=None)
            p1 = int(points_nlogony[0])
            p2 = int(points_nlogony[1])
            n = int(input())
            while n>0:
                other_info = input().split(sep=None)
                alpha = float(other_info[0])
                v = float(other_info[1])
                print(calculate_attack(h, p1, p2, alpha, v))
                n-=1
        except EOFError:
            break


def calculate_attack(h, p1, p2, alpha, v):
    """This function calculates the distance with the supplied data using an equation of MRU ( d = v*t ) and 
    MRUA (yf = y0 + v*t - g*t^2/2 ) putting it all together in one equation

    Args:
        h (float): height
        p1 (int): starting point of the village
        p2 (int): ending point of the village
        alpha (float): lauch angle 
        v (float): initial velocity of the duck

    Returns:
        float: distance where the duck fell
    """
    alpha = alpha*pi/180
    d = (v*math.cos(alpha)*(v*math.sin(alpha)+math.sqrt((v*math.sin(alpha))**2+(2*g*h))))/g
    
    if p1<=d<=p2:
        return str("{:.5f}".format(d))+" -> DUCK"
    else:
        return str("{:.5f}".format(d))+" -> NUCK"


if __name__ == "__main__":
    main()