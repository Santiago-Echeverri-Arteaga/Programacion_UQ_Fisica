"""
tiempo = 0
velocidad = float(input("Ingrese la velocidad inicial: "))
aceleracion = -9.8

while velocidad > 0:
    velocidad += aceleracion*tiempo
    tiempo += 0.0000001
    
print(f"El tiempo buscado es {tiempo}")
"""
#for i in [1,12,"Hola",13,True]:
#    print(i)
suma =0 
for i,j,k in zip(["Andrea Echeverri", "Bob Dylan", "Carlos Vives", 
                      "Duncan Dhu", "Elefante", "Foo Fighters"],
               [120,245,430,123,450,8],
               ["Colombia", "Ecuador", "Argentina", "Bolivia", "Panama", "Venezuela"]):
    if k == "Argentina":
        continue
    print(i,j,k)
    suma += j
    if suma>=1000:
        break
else:
    print("Exito!")
print("Bye")