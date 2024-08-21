class FuncionFisica:
    def __init__(self, nombre, expresion, parametros=None):
        """
        Inicializa la función física.

        :param nombre: Nombre de la función.
        :param expresion: Expresión matemática de la función en formato de cadena.
        :param parametros: Diccionario de parámetros necesarios para la evaluación de la función.
        """
        self.nombre = nombre
        self.expresion = expresion
        self.parametros = parametros if parametros is not None else {}

    def __repr__(self):
        """
        Representación formal de la función.
        """
        return f"FuncionFisica('{self.nombre}', '{self.expresion}', {self.parametros})"

    def __str__(self):
        """
        Representación amigable de la función.
        """
        return f"Función {self.nombre}: {self.expresion}"

    def evaluar(self, x):
        """
        Evalúa la función en un punto x.

        :param x: Punto en el que se evalúa la función.
        :return: Valor de la función en x.
        """
        return eval(self.expresion, {"x": x, **self.parametros})

    def derivada(self, x, h=1e-5):
        """
        Calcula la derivada numérica de la función en el punto x.

        :param x: Punto en el que se evalúa la derivada.
        :param h: Pequeña variación para el cálculo de la derivada.
        :return: Aproximación de la derivada en x.
        """
        return (self.evaluar(x + h) - self.evaluar(x - h)) / (2 * h)

    def metodo_euler(self, x0, y0, dt, t_final):
        """
        Resuelve una ecuación diferencial ordinaria usando el método de Euler.

        :param x0: Valor inicial de la variable independiente.
        :param y0: Valor inicial de la variable dependiente.
        :param dt: Incremento de tiempo.
        :param t_final: Tiempo final para la simulación.
        :return: Lista de tuplas con (x, y) que representan la solución.
        """
        x, y = x0, y0
        resultados = [(x, y)]
        while x < t_final:
            y += self.derivada(y) * dt
            x += dt
            resultados.append((x, y))
        return resultados

    def interpolacion_lineal(self, x1, y1, x2, y2, x):
        """
        Realiza la interpolación lineal entre dos puntos.

        :param x1: Primer punto en x.
        :param y1: Primer punto en y.
        :param x2: Segundo punto en x.
        :param y2: Segundo punto en y.
        :param x: Punto en el que se quiere interpolar.
        :return: Valor interpolado en x.
        """
        return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

    def interpolar(self, puntos, x):
        """
        Interpola un valor en x usando una lista de puntos.

        :param puntos: Lista de tuplas (x, y) ordenadas.
        :param x: Punto en el que se quiere interpolar.
        :return: Valor interpolado en x, o None si x está fuera del rango de puntos.
        """
        for i in range(len(puntos) - 1):
            if puntos[i][0] <= x <= puntos[i+1][0]:
                return self.interpolacion_lineal(puntos[i][0], puntos[i][1], puntos[i+1][0], puntos[i+1][1], x)
        return None

    def newton_raphson(self, x0, tol=1e-5, max_iter=100):
        """
        Encuentra un cero de la función usando el método de Newton-Raphson.

        :param x0: Valor inicial de la búsqueda.
        :param tol: Tolerancia para la convergencia.
        :param max_iter: Número máximo de iteraciones.
        :return: Aproximación del cero de la función, o None si no converge.
        """
        x = x0
        for _ in range(max_iter):
            fx = self.evaluar(x)
            f_prime_x = self.derivada(x)
            if f_prime_x == 0:
                return None  # Evitar división por cero
            x_new = x - fx / f_prime_x
            if abs(x_new - x) < tol:
                return x_new
            x = x_new
        return None

    def integrar_trapecio(self, a, b, n):
        """
        Calcula la integral de la función usando el método del trapecio.

        :param a: Límite inferior de la integral.
        :param b: Límite superior de la integral.
        :param n: Número de subdivisiones.
        :return: Aproximación de la integral en el intervalo [a, b].
        """
        h = (b - a) / n
        sumatoria = 0.5 * (self.evaluar(a) + self.evaluar(b))
        for i in range(1, n):
            sumatoria += self.evaluar(a + i * h)
        return h * sumatoria

    def integrar_simpson(self, a, b, n):
        """
        Calcula la integral de la función usando la regla de Simpson.

        :param a: Límite inferior de la integral.
        :param b: Límite superior de la integral.
        :param n: Número de subdivisiones (debe ser par).
        :return: Aproximación de la integral en el intervalo [a, b].
        """
        if n % 2:
            n += 1  # La regla de Simpson requiere un número par de intervalos
        h = (b - a) / n
        sumatoria = self.evaluar(a) + self.evaluar(b)
        for i in range(1, n, 2):
            sumatoria += 4 * self.evaluar(a + i * h)
        for i in range(2, n-1, 2):
            sumatoria += 2 * self.evaluar(a + i * h)
        return h / 3 * sumatoria

# Definimos una función física simple: f(x) = x^2 - 4
func = FuncionFisica(nombre="Parábola", expresion="x**2 - 4")

# Evaluamos la función en x = 2
print(func.evaluar(2))  # Salida: 0

# Calculamos la derivada numérica en x = 2
print(func.derivada(2))  # Salida: ~4

# Encontramos el cero de la función usando Newton-Raphson
cero = func.newton_raphson(x0=3)
print(cero)  # Salida: ~2

# Calculamos la integral de la función en el intervalo [0, 2] usando el método del trapecio
integral = func.integrar_trapecio(a=0, b=2, n=100)
print(integral)  # Salida: ~-2.67

# Resolución de una ecuación diferencial usando el método de Euler
solucion = func.metodo_euler(x0=0, y0=1, dt=0.1, t_final=2)
print(solucion)  # Lista de tuplas (x, y)
