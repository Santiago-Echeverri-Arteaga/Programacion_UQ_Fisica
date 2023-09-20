def print_pol(pol:list):
    """Función que imprime una lista como si fuera un polinomio

    Args:
        polinomio (list): coeficientes de menor a mayor
    """
    polinomio = pol.copy()
    n = len(polinomio)
    print(f"Su polinomio es {polinomio[0]}", end=' ')
    for i in range(1,n):
        if polinomio[i]<0:
            print(f"- {abs(polinomio[i])}x^{i}",end=' ')
        elif polinomio[i]>0:
            print(f"+ {polinomio[i]}x^{i}",end=' ')
    print('')

n = int(input("Ingrese orden del polinomio: "))
polinomio=[]
for i in range(n+1):
    polinomio.append(float(input(f"Ingrese el coeficiente del término x^{i}: ")))
    
derivada = polinomio[1:]
for i in range(n):
    derivada[i] = derivada[i]*(i+1)
print_pol(polinomio)
print("DERIVANDO...")
print_pol(derivada)