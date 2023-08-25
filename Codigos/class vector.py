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
#print(type(str(21)))
F1=vector(2,3)
F2=vector(-2,3)
print(F1)
print(F2)
Resultado=F1 + F2 +F1 + F2 +F2
print(Resultado.magnitud)
#name=input("Ingrese su nombre: ")
#print("Hola",name)
#edad=float(input("Ingrese su edad: "))
#print("Año",2023-edad)
#print("Tipo de dato edad",type(edad))
#print("Tipo de dato name",type(name))

