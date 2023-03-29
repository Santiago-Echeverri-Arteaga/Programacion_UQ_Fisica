"""
_summary_

Returns:
    _type_: _description_
"""
from string import punctuation
import random
class matriz:
    """La clase matriz ...."""
    def __init__(self, valores):
        self.valores = valores
        n = len(valores)
        m = len(valores[0])
        self.shape = [n, m]
    def __str__(self):
        if self.shape[0]==1:
            respuesta = self._imprimir_vector_(0)
            return(respuesta)
        else:
            respuesta = ""
            for i in range(self.shape[0]-1):
                respuesta = respuesta + self._imprimir_vector_(i)+"\n"
            respuesta = respuesta + self._imprimir_vector_(self.shape[0]-1)
            return(respuesta)
    def _imprimir_vector_(self,fila):
        """Imprimir vector"""
        respuesta = "|"
        for i in range(self.shape[1]-1):
            respuesta = respuesta + str(self.valores[fila][i])
            respuesta = respuesta + " "
            
        respuesta = respuesta + str(self.valores[fila][self.shape[1]-1]) + "|"
        return(respuesta)
        
    def __add__(self, otro):
        if self.shape[0]==1:
            lista = []
            for i in range(self.shape[1]):
                lista.append(self.valores[0][i]+otro.valores[0][i])
            respuesta = matriz([lista])
            return(respuesta)
        else:
            respuesta = self.valores
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    respuesta[i][j] = self.valores[i][j]+otro.valores[i][j]
            return(matriz(respuesta))
    def __mul__(self,otro):
        if (type(otro)==type(self)):
            return(3)
        else:
            return(2)
    def __rmul__(self,otro):
        if (type(otro)==type(self)):
            return(3)
        else:
            return(2)
    def __call__(self, masa):
        a = [self.valores[0][0]/masa, self.valores[0][1]/masa]
        return(a)

def ingresa_vector(N):
    """
    Este es un método que recibe un entero N que corresoponde a la dimension de un vector,
    interactúa con el usuario para solicitarle esa cantidad de valores y finalmente retorna
    el vector.
    
    >>> Vec = ingresa_vector()
    """
    Lista = []
    for i in range(N):
        Lista.append(eval(input("Ingrese valor V_{0} del vector: ".format(i))))
    return matriz([Lista])
       

def main():
    N = int(input("Ingrese numero filas: "))
    V_1 = ingresa_vector(N)
    V_2 = ingresa_vector(N)
    resultante = V_1 + V_2
    m = 2
    print("Aceleracion",resultante(m))
    #print("V2",V2())
    print()
    #V2= matriz([L_2])
    #print(type(V1+V2))
    #print(V1+V2)

def print_funcion(x,f):
    print(f(x))

def palabra_a_vector(palabra:str):
    for i in punctuation:
        palabra = palabra.replace(i,"")
    tildes = "áéíóúÁÉÍÓÚ"
    for i in range(len(tildes)):
        palabra = palabra.replace(tildes[i],"aeiouAEIOU"[i])
    palabra = palabra.split()
    vector = []
    for i in palabra:
        vector.append(len(i))
    return(vector)


#import math
#A = 10
#w = 3*math.pi/2
#f = math.pi/2
#print_funcion(1,lambda t:A*math.sin(w*t+f))
#main()
print(palabra_a_vector("Ésta: Mi. palabra;{"))
