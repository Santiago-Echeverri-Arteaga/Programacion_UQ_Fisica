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
        if parametros!=None:
            self.parametros = parametros
        else:
            self.parametros = {}

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
        
    def evaluar(self, x, y=None):
        import math
        # Evaluar la expresión en el contexto de x (y también y si es necesario)
        return eval(self.expresion, {"x": x, "y": y, "sin": math.sin})

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
            y += self.evaluar(x, y) * dt  # y_n+1 = y_n + f(x_n, y_n) * dt
            x += dt
            resultados.append((x, y))
        return resultados

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
        print(f"Se alcanzó el máximo de iteraciones ({max_iter:d}) sin obtener una respuesta dentro de la toleracia establecida ({tol:.2e})")
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



# Definimos una función física simple: f(x) = x^2 - 4
func = FuncionFisica(nombre="Parábola", expresion="x**2 - 4")

# Evaluamos la función en x = 2
print(f"El valor de la función evaluada es: {func.evaluar(2)}")  # Salida: 0

# Calculamos la derivada numérica en x = 2
print(f"La derivada vale {func.derivada(2):.2f}")  # Salida: ~4

# Encontramos el cero de la función usando Newton-Raphson
cero = func.newton_raphson(x0=3)
print(f"Se encuentra el cero de la función: {cero}")  # Salida: ~2

# Calculamos la integral de la función en el intervalo [0, 2] usando el método del trapecio
integral = func.integrar_trapecio(a=0, b=2, n=100)
print(f"la integral en el intervalo [0,2] vale: {integral}")  # Salida: ~-2.67

# Resolución de una ecuación diferencial usando el método de Euler
solucion = func.metodo_euler(x0=0, y0=1, dt=0.001, t_final=2)
print(f"Solución de la EDO: {solucion}")  # Lista de tuplas (x, y)

# solución exacta es x**3/3-4*x+1 