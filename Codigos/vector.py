class matriz:
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
V1= matriz([[1,2,3, 5, 690, 0],[100,200,300, 500, 600, 0]])
V2= matriz([[10,20,30, 0, 10, 30],[11,21,31, 0, 10, 30]])
#print(type(V1+V2))
print(V1+V2)