def main():
    condition = True
    while condition == True:
        t = int(input())
        if 1<=t<=10**4:
            condition = False
            
    while t!=0:
        first_string = input().split(sep=None)
        l = int(first_string[0])
        r = int(first_string[1])
        x = int(first_string[2])
        second_string = input().split(sep=None)
        a = int(second_string[0])
        b = int(second_string[1])
        if (1<=t<=10**4) and (-10**9<=l<=r<=10**9) and (1<=x<=10**9) and len(first_string)==3 and len(second_string)==2:
            print(variateThemp(l, r, x, a, b))
            t -=1


def variateThemp(l,r,x,a,b):
    cont = 0
    if a == b:
        pass
    elif abs(a-b)>=x:
        cont = 1
    elif (min(a,b) - l>=x) or (r - max(a,b)>=x):
        cont = 2
    elif ((r - b)>=x and (a - l)>=x) or ((r - a)>=x and (b - l)>=x):
        cont = 3
    else:
        cont = -1
    return cont


if __name__ == "__main__":
    main()