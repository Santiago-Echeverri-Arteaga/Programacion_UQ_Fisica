#Importa librería para ordenar aleatoriamente los estudiantes
import random
# Se crea lista de estudiantes como números entre 1 y 10 
# Lista oficial
estudiantes = ["AGUILAR CARDENAS SANTIAGO",
         "ARIAS IGUITA JUAN DIEGO",
         "BERMUDEZ CEBALLOS DAIAN ALEJANDRA",
         "BOLIVAR LAZO CAMILO",
         "GARCÍA BARRERA JHON SEBASTIAN",
         "JIMÉNEZ HURTADO JORGE LUIS",
         "MARTINEZ GOMEZ NATALIA ISABEL",
         "PAZ HORMIGA JUAN JOSE",
         "RIVERA MARTINEZ DAVID SEBASTIAN",
         "SALAZAR QUINTERO KAROL VIVIANA"]
# Ordena aleatoriamente
random.shuffle(estudiantes)
# Selecciona los estudiantes
for e,p in zip(estudiantes, "ABCDEFGHIJ"):
     print("El parcial {} le corresponde al estudiante {}".format(p,e))