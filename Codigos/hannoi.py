def torres_hanoi(n:int, origen:str, auxiliar:str, destino:str):
    torres_hanoi.count+=1
    if n == 1:
        print(f"Mover disco 1 de la torre {origen} a la torre {destino}")
        return
    torres_hanoi(n - 1, origen, destino, auxiliar)
    print(f"Mover disco {n} de la torre {origen} a la torre {destino}")
    torres_hanoi(n - 1, auxiliar, origen, destino)

torres_hanoi.count=0

n = int(input("Ingrese el número de discos: "))
torres_hanoi(n, 'A', 'B', 'C')
print(f"Número de movimientos requeridos {torres_hanoi.count}")

