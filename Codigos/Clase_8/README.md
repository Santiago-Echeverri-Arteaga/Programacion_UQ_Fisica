# Física Computacional con Python

Este repositorio contiene la implementación de tres clases fundamentales para modelar sistemas físicos en Python: `Vector`, `Particula`, y `SistemaParticulas`. Estas clases permiten la simulación y el análisis de sistemas dinámicos en el espacio 2D y 3D.

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
