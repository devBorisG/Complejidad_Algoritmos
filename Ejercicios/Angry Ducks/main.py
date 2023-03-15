import math

"""Global variable definitions"""
g = 9.80665
pi = 3.14159


def main():
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
    alpha = alpha*pi/180
    d = (v*math.cos(alpha)*(v*math.sin(alpha)+math.sqrt((v*math.sin(alpha))**2+(2*g*h))))/g
    
    if p1<=d<=p2:
        return str("{:.5f}".format(d))+" -> DUCK"
    else:
        return str("{:.5f}".format(d))+" -> NUCK"


if __name__ == "__main__":
    main()