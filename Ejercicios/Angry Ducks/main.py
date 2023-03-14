import math

g = 9.80665
pi = 3.14159

def main():
    cond = True
    while cond == True:
        h = float(input())
        if 1<=h<=150:
            cond = False
    cond = True
    while cond == True:
        points_nlogony = input().split(sep=None)
        p1 = int(points_nlogony[0])
        p2 = int(points_nlogony[1])
        if 1<=p1<=9999 and 1<=p2<=9999:
            cond=False
    cond=True
    while cond == True:
        n = int(input())
        if 1<=n<=100:
            cond = False
    while n>0:
        other_info = input().split(sep=None)
        alpha = float(other_info[0])
        v = float(other_info[1])
        if 1<=alpha<=180 and 1<=v<=150:
            print(calculate_attack(h,p1,p2,alpha,v))
            n-=1


def calculate_attack(h, p1, p2, alpha, v):
    t = flight_time(h, v, alpha)
    d = max_distance(v, t, alpha)
    
    if p1<=d<=p2:
        return str("{:.5f}".format(d))+" -> DUCK"
    else:
        return str("{:.5f}".format(d))+" -> NUCK"


def flight_time(h, v, alpha):
    
    vy = v*math.sin(degree_to_radians(alpha))
    quadratic_formula = (vy + (math.sqrt(vy**2-(4*g/2*-h))))/g
    return quadratic_formula


def max_distance(v, t, alpha):
    vx = v*math.cos(degree_to_radians(alpha))
    return vx*t


def degree_to_radians(alpha):
    return alpha*pi/180


if __name__ == "__main__":
    main()