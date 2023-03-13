import math

def main():
    h = float(input())
    
    points_nlogony = input().split(sep=None)
    p1 = int(points_nlogony[0])
    p2 = int(points_nlogony[1])
    
    n = int(input())
    
    while n>0:
        other_info = input().split(sep=None)
        alpha = float(other_info[0])
        v = float(other_info[1])
        
        print(calculate_attack(h,p1,p2,alpha,v))
        
        n-=1
    
    
def calculate_attack(h, p1, p2, alpha, v):
    g = 9.80665
    pi = 3.14159
    
    t = flight_time(h, g)
    d = max_distance(v, t, alpha, pi)
    
    if p1<=d<=p2:
        return "DUCK -> "+str("{:.5f}".format(d))
    else:
        return "NUCK -> "+str("{:.5f}".format(d))
    
def flight_time(h, g):
    return math.pow((2*h)/g,1/2)

def max_distance(v, t, alpha, pi):
    vx = v*math.cos(degree_to_radians(alpha, pi))
    
    return vx*t
    
def degree_to_radians(alpha, pi):
    return alpha*pi/180

if __name__ == "__main__":
    main()