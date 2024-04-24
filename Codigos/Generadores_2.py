def contador(max):
    print("Dentro del contador")
    n=0
    while n<max:
        print(f"Dentro del contador - yield viene con n={n}")
        yield(n)
        print(f"Dentro del contador - retomando después de yield")
        n+=1
    print(f"Dentro del contador - Terminado")
    yield("FIN")

print("Instanciando contador")
mycont = contador(3)
print(f"Contador={mycont}")
print("Contador Instanciado")

#for i in mycont:
#    print(f"Valor leido del iterador={i}")

def alleven(max):
    n=0
    while n<max:
        yield(n)
        n+=2
#pares = alleven()
#for i in pares:
    #print(i)
    #print(f"Salida del next={next(pares)}")
    #if i == 100:
     #   break
lista= range(10)
por_dos = map(lambda x:2*x, lista)
filtro = filter(lambda x:x%4==0,por_dos)
print(filtro)
from operator import add
from functools import reduce

print(reduce(add,filtro))