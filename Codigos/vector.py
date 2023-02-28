class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dim = 2
        self.norm = (x**2 + y**2)**0.5
    def __str__(self):
        respuesta = "(" + str(self.x) + ", " + str(self.y) +")"
        return(respuesta)
    def __add__(self, other):
        respuesta = vector(self.x+other.x, self.y+other.y)
        return(respuesta)
V1= vector(1,2)
V2= vector(3,4)
print(V1+V2+V1+V2+V2)
