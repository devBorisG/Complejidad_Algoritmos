# Whuile para evaluar que no se salga de los rangos y la otra condicion
# else para decir que es imposible (-1)
# dos if para saber halalr el numero que sumarle o restarle si b es mayor o menor
# dos if adicionales para saber si b esta por encima o debajo de a para sumarle o restarle el minimo
# se necesita uan varible adicional "c"

def main():
    t = int(input())
    
    
    for i in range(t):
        l = int(input())
        r = int(input())
        x = int(input())
        a = int(input())
        b = int(input())
        print(variateThemp(l, r, x, a, b))
    
    
def variateThemp(l,r,x,a,b):
    c = 0
    cont = 0
    while a!=b:
        if abs(a-b)>=x:
            cont+=1
        elif a>b:
            if cont == 0:
                a = a - x
                cont += 1
            else:
                while a != b:
                    a = a + 1
                else:
                    cont += 1
        elif a<b:
            c = a + x
            a = c
            cont += 1
            while a != b:
                a = a - 1
            else:
                cont += 1
        else:
            cont = -1
    
    return cont
    
    
if __name__ == "__main__":
    main()