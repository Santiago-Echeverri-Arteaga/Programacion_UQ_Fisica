from typing import Any


class vector:
    """
    Clase vector 3D en espacio Euclideano. Permite realizar las operaciones
    básicas de los vectores necesarias en mecánica.
    """
    def __init__(self, componente_x, componente_y, componente_z):
        self.x=componente_x
        self.y=componente_y
        self.z=componente_z
        self.magnitud= (self.x**2+self.y**2+self.z**2)**0.5
    def __str__(self):
        nombre = f"Yo soy ({self.x:5.2f}\t{self.y:5.2f}\t{self.z:5.2f})"
        return nombre
    def __add__(self, other):
        vector_respuesta = vector(self.x+other.x, self.y+other.y, self.z+other.z)
        return vector_respuesta
    def __sub__(self, other):
        vector_respuesta = vector(self.x-other.x, self.y-other.y, self.z-other.z)
        return vector_respuesta
    def aceleracion(self, masa):
        vector_respuesta = vector(self.x/masa, self.y/masa, self.z/masa)
        return vector_respuesta
    def __mul__(self,other):
        if type(other)==type(2) or type(other)==type(2.1):
            vector_respuesta = vector(self.x*other, self.y*other, self.z*other)
            return vector_respuesta
        else:
            raise ValueError("No se puede realizar la multiplicación")
    def __rmul__(self,other):
        return self.__mul__(other)

v1 = vector(10,2,3)
v2 = vector(0,3,5)
v3 = vector(-10,-3,-15)
v4 = 2*v1+4*v2-5*v3
print(v4)
print(v4.magnitud)
print(v4.aceleracion(10))
