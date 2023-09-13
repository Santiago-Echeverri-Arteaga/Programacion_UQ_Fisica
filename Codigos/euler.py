# Define la función f(x, y)
f = lambda x, y: x - y

def euler_method(f, x0, y0, x_final, h):
    x_values = [x0]
    y_values = [y0]

    while x0 < x_final:
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values

# Ejemplo de uso:
import matplotlib.pyplot as plt



# Valores iniciales y condiciones
x0 = 0
y0 = 1
x_final = 5
h = 0.1

x_values, y_values = euler_method(f, x0, y0, x_final, h)

# Grafica la solución
plt.plot(x_values, y_values, label='Solución aproximada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
