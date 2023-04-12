def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")
                return output   # SI ESTA LINEA NO ESTÁ LA FUNCIÓN DECORADA NO RETORNA NADA!!!!
        return decorador_funcion
    return decorador_log

@log('ficherosalida.log')
def suma(a, b):
    return a + b

@log('ficherosalida.log')
def resta(a, b):
    return a - b

@log('ficherosalida.log')
def multiplicadivide(a, b, c):
    return a*b/c

a=suma(10, 30)
b=resta(7, 23)
c=multiplicadivide(5, 10, 2)
print(a,b,c)