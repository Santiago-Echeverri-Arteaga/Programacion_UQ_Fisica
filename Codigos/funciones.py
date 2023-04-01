def funcion(a, *args, b=0, **kwargs):
    print("a=",a)
    print("b=",b)
    print("args=",args)
    print("kwargs=",kwargs)
    print("-"*80)

def func(a,b):
    respuesta1 = [a+b,a+2*b]
    respuesta2 = a*b
    respuesta3 = "Hola Mundo"
    return[respuesta1,respuesta2, respuesta3]

def variables(a):
    a= a.copy()
    a.append(2)
    print(a)
    
    return()

a=[1,2]
b=a.copy()
a.append(12)
b.append(156)
print(a)
print(b)
#print(a)
#variables(a)
#print(a)
#uno,dos,tres = func(2,3)
#print("uno",uno)
#print("dos",dos)
#print("tres",tres)
#funcion(10,20,30,40,50,60,70,b=5,color="azul", categoria="estudiante")