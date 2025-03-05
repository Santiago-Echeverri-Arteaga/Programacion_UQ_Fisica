
def factorial(n):
  """Calcula el factorial de un número n.
  n debe ser un entero no negativo.
  
  >>> factorial(5)
  120
  """
  if n==0:
    return(1)
  else:
    return(n*factorial(n-1))
  

#  resultado = 1
#  for i in range(1,n+1):
#      resultado *= i
#  return(resultado)

#for i in range(10+1):
#  print(f"{i}!={factorial(i)}")

cuadratica = lambda a,b,c,x: a*x**2+b*x+c

#print(cuadratica(1,4,5,1))

N = int(input("Digame cuántos términos desea de la secuencia de fibonacci: "))
def fibo(N):
  if N<0:
    print("ERROR")
    return
  elif N==0:
    return(1)
  elif N==1:
    return(1)
  else:
    return(fibo(N-1)+fibo(N-2))

for i in range(N+1):
  print(fibo(i), end=" ")
print("")
"""
if N<0:
  print("ERROR: Número invalido")
elif N==0 or N==1:
  print(1, end=" ")
else:
  a,b = 1,1
  print(1,1, end=" ")
  for i in range(2,N+1):
    resultado = a + b
    print(resultado, end=" ")
    a,b = b, resultado
  print("")
"""
#MaxIter = int(input("Número máximo de iteraciones: "))
#Tol = float(input("Ingrese el máximo error que tolera: "))
#x = float(input("Ingrese ángulo en radianes: "))
#resultado = x
#for i in range(1,MaxIter):
#  Cnp1 = ((-1)**(i+1))*(x**(2*(i+1)+1))/factorial(2*(i+1)+1)
#  if abs(Cnp1) < Tol:
#    break
  #print(f"n={2*i+1}, n!={factorial(2*i+1)}")
#  Cn = ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)
#  resultado = resultado + Cn
#  print(Cn)
#else:
#  print(f"WARNING: No se alcanzó la tolerancia deseada con {MaxIter} iteraciones")
#print(f"sin({x})={resultado}")