import random

def pregunta_al_azar(n1, n2):
    """Realiza una pregunta de multiplicación al azar entre n1 y n2 y se la pregunta al usuario.
    n1: Número entero que define el número más pequeño que le preguntará
    n2: Número entero que define el número más grande que le preguntará
    Retorna la respuesta del usuario y la del correcta
    
    >>> pregunta_al_azar(1,5)
    ¿Cuánto es 2*3? 5
    5, 6"""
    a = random.randint(n1,n2)
    b = random.randint(n1,n2)
    respuesta = int(input(f"¿Cuánto es {a}*{b}? "))
    verdad = a*b
    return(respuesta, verdad)

def ronda_del_juego(vidas,intentos, n1=1, n2=10):
    respuesta, verdad = pregunta_al_azar(n1, n2)
    if respuesta == verdad:
        print("Felicitaciones")
    else:
        print("ERROR: Pierdes una vida")
        vidas -= 1
    intentos += 1
    return(vidas,intentos)


rondas = 20
vidas =3
intentos =0
while intentos < rondas and vidas > 0:
    print("*"*20)
    print(f"Inicio de ronda {intentos+1}")
    print(f"Vidas: {vidas}")
    print(f"Intentos: {intentos}")
    vidas, intentos = ronda_del_juego(vidas, intentos,n1=1, n2=10)
if vidas>0:
    print("Has ganado!")
else:
    print("Perdiste :(")