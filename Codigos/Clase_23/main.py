# main.py

# Importar el paquete y los módulos
import paquete_de_python as papy

# Usar las funciones de modulo1 y modulo2, que están expuestas en __init__.py
papy.funcion_modulo1()
papy.funcion_modulo2()

# También puedes importar subpaquetes y sus funciones
#from paquete_de_python.subpaquete import funcion_modulo3
#funcion_modulo3()

# Cuando se agrega al init todo lo que hay en los modulos
papy.funcion_modulo3()

# Cuando se agrega en init el modulo pero no su contenido
#papy.modulo3.funcion_modulo3()
print(dir(papy))