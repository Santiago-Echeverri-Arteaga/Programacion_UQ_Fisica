import math

class Vector:
    def __init__(self, x, y, z=0):
        """
        Inicializa un vector en el espacio 3D.

        :param x: Componente x del vector.
        :param y: Componente y del vector.
        :param z: Componente z del vector (opcional, por defecto 0).
        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """
        Representación formal del vector.
        """
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __str__(self):
        """
        Representación amigable del vector.
        """
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """
        Suma de dos vectores.

        :param other: Otro vector.
        :return: Vector resultante de la suma.
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        Resta de dos vectores.

        :param other: Otro vector.
        :return: Vector resultante de la resta.
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        """
        Multiplicación de un vector por un escalar (vector * escalar).

        :param scalar: Escalar por el cual se multiplica el vector.
        :return: Vector resultante de la multiplicación.
        """
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        """
        Multiplicación de un vector por un escalar (escalar * vector).

        :param scalar: Escalar por el cual se multiplica el vector.
        :return: Vector resultante de la multiplicación.
        """
        return self.__mul__(scalar)

    def __call__(self, *args):
        """
        Permite evaluar el vector o realizar operaciones con otro vector.
        
        :param args: Puede ser un punto específico o un vector.
        :return: Valor o vector resultante.
        """
        if len(args) == 1 and isinstance(args[0], Vector):
            return self + args[0]  # Ejemplo: sumar dos vectores al ser llamados
        elif len(args) == 2:
            return self.dot(args[0]) * args[1]  # Ejemplo: evaluar el producto punto con un escalar
        else:
            return None

    def magnitude(self):
        """
        Calcula la magnitud del vector.

        :return: Magnitud del vector.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot(self, other):
        """
        Calcula el producto punto con otro vector.

        :param other: Otro vector.
        :return: Producto punto de los dos vectores.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """
        Calcula el producto cruzado con otro vector.

        :param other: Otro vector.
        :return: Vector resultante del producto cruzado.
        """
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)


import numpy as np

class Particula:
    def __init__(self, nombre, masa, posicion, velocidad):
        """
        Inicializa una partícula.

        :param nombre: Nombre de la partícula.
        :param masa: Masa de la partícula.
        :param posicion: Posición de la partícula (Vector).
        :param velocidad: Velocidad de la partícula (Vector).
        """
        self.nombre = nombre
        self.masa = masa
        self.posicion = posicion
        self.velocidad = velocidad

    def __repr__(self):
        return f"Particula('{self.nombre}', masa={self.masa}, posicion={self.posicion}, velocidad={self.velocidad})"

    def __str__(self):
        return f"{self.nombre}: Masa={self.masa}, Posición={self.posicion}, Velocidad={self.velocidad}"

    def energia_cinetica(self):
        """
        Calcula la energía cinética de la partícula.

        :return: Energía cinética (float).
        """
        return 0.5 * self.masa * self.velocidad.magnitude() ** 2

    def actualizar_posicion(self, dt):
        """
        Actualiza la posición de la partícula según su velocidad.

        :param dt: Incremento de tiempo.
        """
        self.posicion = self.posicion + self.velocidad * dt

    def aplicar_fuerza(self, fuerza, dt):
        """
        Aplica una fuerza a la partícula y actualiza su velocidad.

        :param fuerza: Fuerza aplicada (Vector).
        :param dt: Incremento de tiempo.
        """
        aceleracion = fuerza * (1 / self.masa)
        self.velocidad = self.velocidad + aceleracion * dt


class SistemaParticulas:
    def __init__(self):
        """
        Inicializa un sistema de partículas vacío.
        """
        self.particulas = []
        self.tiempo = 0.0

    def agregar_particula(self, particula):
        """
        Agrega una partícula al sistema.

        :param particula: Objeto de tipo Particula.
        """
        self.particulas.append(particula)

    def __repr__(self):
        return f"SistemaParticulas({self.particulas})"

    def __str__(self):
        return f"Sistema con {len(self.particulas)} partículas"

    def energia_total(self):
        """
        Calcula la energía cinética total del sistema.

        :return: Energía cinética total (float).
        """
        return sum(p.energia_cinetica() for p in self.particulas)

    def aplicar_fuerza_externa(self, fuerza):
        """
        Aplica una fuerza externa a todas las partículas del sistema.

        :param fuerza: Fuerza externa (Vector).
        """
        for particula in self.particulas:
            particula.aplicar_fuerza(fuerza, 1)  # Aplicar fuerza durante 1 segundo

    def actualizar(self, dt):
        """
        Actualiza las posiciones de todas las partículas en el sistema.

        :param dt: Incremento de tiempo.
        """
        for particula in self.particulas:
            particula.actualizar_posicion(dt)
        self.tiempo += dt

    def simular(self, dt, t_final):
        """
        Simula el sistema de partículas hasta el tiempo final.

        :param dt: Incremento de tiempo.
        :param t_final: Tiempo final de la simulación.
        """
        while self.tiempo < t_final:
            self.actualizar(dt)
            print(f"Tiempo: {self.tiempo:.2f} s, Energía total: {self.energia_total():.2f} J")




# Definir dos vectores en el espacio 3D
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Mostrar los vectores
print(v1)  # Salida: (1, 2, 3)
print(v2)  # Salida: (4, 5, 6)

# Sumar y restar vectores
v_sum = v1 + v2
v_diff = v1 - v2
print(v_sum)   # Salida: (5, 7, 9)
print(v_diff)  # Salida: (-3, -3, -3)

# Multiplicación por un escalar
v_scaled = v1 * 2
print(v_scaled)  # Salida: (2, 4, 6)

# Magnitud del vector
print(v1.magnitude())  # Salida: 3.7416573867739413

# Producto punto
dot_product = v1.dot(v2)
print(dot_product)  # Salida: 32

# Producto cruzado
cross_product = v1.cross(v2)
print(cross_product)  # Salida: (-3, 6, -3)

# Uso del método __call__
result = v1(v2)  # Suma de dos vectores usando __call__
print(result)  # Salida: (5, 7, 9)


# Ejemplo de uso con las clases Vector y Particula
if __name__ == "__main__":
    # Crear un par de vectores para la posición y la velocidad
    p1_pos = Vector(0, 0, 0)
    p1_vel = Vector(1, 0, 0)
    
    p2_pos = Vector(0, 1, 0)
    p2_vel = Vector(0, -1, 0)

    # Crear partículas
    p1 = Particula(nombre="Partícula 1", masa=1.0, posicion=p1_pos, velocidad=p1_vel)
    p2 = Particula(nombre="Partícula 2", masa=2.0, posicion=p2_pos, velocidad=p2_vel)

    # Crear un sistema de partículas
    sistema = SistemaParticulas()
    sistema.agregar_particula(p1)
    sistema.agregar_particula(p2)

    # Simular el sistema durante 10 segundos con un paso de tiempo de 1 segundo
    sistema.simular(dt=1, t_final=10)
