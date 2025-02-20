
def factorial(n):
  """Calcula el factorial de un número n.
  n debe ser un entero no negativo.

  >>> factorial(5)
  120
  """
  resultado = 1
  for i in range(1,n+1):
      resultado *= i
  return(resultado)
#for i in range(10+1):
#  print(f"{i}!={factorial(i)}")

cuadratica = lambda a,b,c,x: a*x**2+b*x+c

print(cuadratica(1,4,5,1))