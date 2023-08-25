from typing import Any


class vector:
    """Clase vector en 2D con coordenadas cartesianas y polares.
    Permite suma entre vectores y multiplicación"""
    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.magnitud = (a**2+b**2)**0.5
    def __add__(self, otro):
        F3=vector(self.x+otro.x, self.y+otro.y)
        return(F3)
    def __str__(self):
        cadena="["+str(self.x)+" "+str(self.y)+"]"
        return(cadena)
    def __abs__(self):
        return(self.magnitud)
    def __call__(self, m:float):
        """Metodo que recibe la masa m como flotante y retorna un vector con
        correspondiente al vector ingresado dividido la masa

        Args:
            m (float): masa
        """
        return(vector(self.x/m, self.y/m))
#print(type(str(21)))
F1=vector(2,3)
print(abs(F1))
#F2=vector(-2,3)
#print(F1(3))
if F1(2).magnitud==0:
    print("Está en equilibrio")
else:
    print("No esta en equilibrtio")
#print(F2)
#Resultado=F1 + F2 +F1 + F2 +F2
#print(Resultado.magnitud)
#name=input("Ingrese su nombre: ")
#print("Hola",name)
#edad=float(input("Ingrese su edad: "))
#print("Año",2023-edad)
#print("Tipo de dato edad",type(edad))
#print("Tipo de dato name",type(name))

