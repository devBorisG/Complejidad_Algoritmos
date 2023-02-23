# Whuile para evaluar que no se salga de los rangos y la otra condicion
# else para decir que es imposible (-1)
# dos if para saber halalr el numero que sumarle o restarle si b es mayor o menor
# dos if adicionales para saber si b esta por encima o debajo de a para sumarle o restarle el minimo
# se necesita uan varible adicional "c"

def main():
    t = int(input)
    firstLine = int(input)
    secondLine = int(input)
    for i in range(t+1):
        variateThemp(firstLine[0],firstLine[1],firstLine[2],secondLine[0],secondLine[1])
    
def variateThemp(l,r,x,a,b):
    print(l,r,x,a,b)
    