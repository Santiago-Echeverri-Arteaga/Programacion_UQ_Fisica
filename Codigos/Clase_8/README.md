# Ejemplos de clases en Python (Ideas para el proyecto I)

En esta carpeta se encuentran la implementación de cuatro clases fundamentales para modelar sistemas físicos en Python: `Vector`, `Particula`, `SistemaParticulas`, y `FunciónFisica`. Estas clases permiten la simulación y el análisis de sistemas dinámicos en el espacio 2D y 3D, así como la manipulación y análisis de funciones matemáticas aplicadas a la física.



## Clases Implementadas

### 1. `Vector`

La clase `Vector` representa un vector en el espacio tridimensional, con métodos para realizar operaciones básicas como suma, resta, multiplicación por un escalar, y cálculos más avanzados como producto punto y producto cruzado.

#### Métodos Principales:
- `__repr__` y `__str__`: Representación formal y amigable del vector.
- `__add__`, `__sub__`: Suma y resta de vectores.
- `__mul__`, `__rmul__`: Multiplicación de un vector por un escalar.
- `magnitude()`: Calcula la magnitud del vector.
- `dot(other)`: Calcula el producto punto entre dos vectores.
- `cross(other)`: Calcula el producto cruzado entre dos vectores.
- `__call__`: Permite evaluar el vector o realizar operaciones adicionales cuando se llama al objeto como función.

#### Ejemplo de Uso:

```python
# Definir dos vectores en el espacio 3D
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Sumar y restar vectores
v_sum = v1 + v2
v_diff = v1 - v2

# Multiplicación por un escalar
v_scaled = v1 * 2

# Magnitud del vector
magnitud_v1 = v1.magnitude()

# Producto punto
dot_product = v1.dot(v2)

# Producto cruzado
cross_product = v1.cross(v2)
```

### 2. `Particula`
La clase `Particula` modela una partícula en el espacio, con atributos como masa, posición (`vector`), y velocidad (`vector`). Incluye métodos para calcular la energía cinética de la partícula y actualizar su posición y velocidad bajo la influencia de fuerzas externas.
#### Métodos Principales:
- `__repr__` y `__str__`: Representación formal y amigable de la partícula.
- `energia_cinetica()`: Calcula la energía cinética de la partícula.
- `actualizar_posicion(dt)`: Actualiza la posición de la partícula en función de su velocidad y el tiempo dt.
- `aplicar_fuerza(fuerza, dt)`: Aplica una fuerza a la partícula y actualiza su velocidad.

#### Ejemplo de Uso:
```python

# Crear un vector de posición y un vector de velocidad
pos = Vector(0, 0, 0)
vel = Vector(1, 0, 0)

# Crear una partícula
p = Particula(nombre="Partícula 1", masa=1.0, posicion=pos, velocidad=vel)

# Calcular la energía cinética
energia = p.energia_cinetica()

# Actualizar la posición de la partícula después de 1 segundo
p.actualizar_posicion(dt=1)

# Aplicar una fuerza a la partícula durante 1 segundo
fuerza = Vector(0, 10, 0)
p.aplicar_fuerza(fuerza, dt=1)
```

### 3. `SistemaParticulas`
La clase `SistemaParticulas` gestiona un conjunto de partículas y permite simular su evolución en el tiempo. Incluye métodos para agregar partículas al sistema, calcular la energía total, aplicar fuerzas externas y actualizar las posiciones de todas las partículas.
Métodos Principales:
- `__repr__` y `__str__`: Representación formal y amigable del sistema.
- `agregar_particula(particula)`: Agrega una nueva partícula al sistema.
- `energia_total()`: Calcula la energía cinética total del sistema.
- `aplicar_fuerza_externa(fuerza)`: Aplica una fuerza externa uniforme a todas las partículas del sistema.
- `actualizar(dt)`: Actualiza la posición de cada partícula en función de su velocidad.
- `simular(dt, t_final)`: Simula la evolución temporal del sistema desde el tiempo actual hasta t_final.

#### Ejemplo de uso:

```python
# Crear vectores de posición y velocidad para dos partículas
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
```

### 4. `FunciónFisica`

La clase `FunciónFisica` permite modelar funciones matemáticas que describen fenómenos físicos. Los métodos de esta clase permiten realizar operaciones como la evaluación de la función, cálculo de derivadas numéricas, integración, interpolación, y la resolución de ecuaciones diferenciales.

#### Métodos Principales:
- `__repr__` y `__str__`: Representación formal y amigable de la función.
- `evaluar(x)`: Evalúa la función en un punto `x`.
- `derivada(x, h=1e-5)`: Calcula la derivada numérica en el punto `x`.
- `metodo_euler(x0, y0, dt, t_final)`: Resuelve una ecuación diferencial ordinaria usando el método de Euler.
- `interpolacion_lineal(x1, y1, x2, y2, x)`: Realiza la interpolación lineal entre dos puntos.
- `interpolar(puntos, x)`: Interpola un valor en `x` usando una lista de puntos.
- `newton_raphson(x0, tol=1e-5, max_iter=100)`: Encuentra un cero de la función usando el método de Newton-Raphson.
- `integrar_trapecio(a, b, n)`: Calcula la integral de la función usando el método del trapecio.
- `integrar_simpson(a, b, n)`: Calcula la integral de la función usando la regla de Simpson.

#### Ejemplo de Uso:

```python
# Definir una función física simple: f(x) = x^2 - 4
func = FuncionFisica(nombre="Parábola", expresion="x**2 - 4")

# Evaluar la función en x = 2
print(func.evaluar(2))  # Salida: 0

# Calcular la derivada numérica en x = 2
print(func.derivada(2))  # Salida: ~4

# Encontrar el cero de la función usando Newton-Raphson
cero = func.newton_raphson(x0=3)
print(cero)  # Salida: ~2

# Calcular la integral de la función en el intervalo [0, 2] usando el método del trapecio
integral = func.integrar_trapecio(a=0, b=2, n=100)
print(integral)  # Salida: ~-2.67

# Resolución de una ecuación diferencial usando el método de Euler
solucion = func.metodo_euler(x0=0, y0=1, dt=0.1, t_final=2)
print(solucion)  # Lista de tuplas (x, y)
```
