def main():
    """Input the numbers of cases, then Input the first line that constains the limits 'l' and 'r'
    and the minimum number of movements that can be made. Then the second line contains the initial
    temperature 'a' and final temperature 'b'; calls the function that returns the minimum number of steps to reach 'b'
    """
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
    """It makes 4 important comparisons, first to know if the temperatures a and b are equal, second to know if 
    the subtraction between these two is greater than x which would mean that a movement can be made, the other 
    two comparisons are playing with l, r, a, b always comparing with x to know if it makes 2 or 3 movements.
    If it does not pass through any of the 4 filters it means that it is impossible. 

    Args:
        l (int): represents the lower limit of the thermostat
        r (int): represents the upper limit of the thermostat
        x (int): represents the minimum number of movements
        a (int): represents the initial temperature of the thermostat
        b (int): represents the final temperature of the thermostat

    Returns:
        int: number of movements required
    """
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