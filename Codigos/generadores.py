def all_even(N):
    n = 0
    while n<=N:
        yield(n)
        n += 2

    
    
# Crear un objeto generador
mi_generador = all_even(10)
mi_generador_2 = {(i, i**2, i**3):3*i-8 for i in mi_generador}
print(mi_generador_2)
# Iterar a través del generador usando un bucle for
#for numero in mi_generador_2:
#    print(numero)
    