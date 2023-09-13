def runge_kutta_4th_order(f, x0, y0, x_final, h):
    x_values = [x0]
    y_values = [y0]

    while x0 < x_final:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)

        y0 = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        x0 = x0 + h

        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values

# Ejemplo de uso:
import matplotlib.pyplot as plt

# Define la función f(x, y)
def f(x, y):
    return x - y

# Valores iniciales y condiciones
x0 = 0
y0 = 1
x_final = 5
h = 0.1

x_values, y_values = runge_kutta_4th_order(f, x0, y0, x_final, h)

# Grafica la solución
plt.plot(x_values, y_values, label='Solución aproximada RK4')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
