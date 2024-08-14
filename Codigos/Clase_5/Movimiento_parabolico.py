"""
Ejemplo 1: Simulación de Movimiento Parabólico
Este código simula la trayectoria de un proyectil lanzado desde un cierto ángulo y velocidad inicial.
"""
import math

# Parámetros iniciales
v0 = 20  # velocidad inicial en m/s
angulo = 45  # ángulo de lanzamiento en grados
g = 9.81  # aceleración debida a la gravedad en m/s^2

# Convertir el ángulo a radianes
angulo_rad = math.radians(angulo)

# Componentes de la velocidad inicial
vx = v0 * math.cos(angulo_rad)
vy = v0 * math.sin(angulo_rad)

# Tiempo total de vuelo
t_vuelo = (2 * vy) / g

# Calcular la posición en varios puntos de tiempo
t = 0
dt = 0.1  # incremento de tiempo en segundos
x_max = 0  # para almacenar la distancia máxima

print(f"Tiempo (s)\tX (m)\tY (m)")
while t <= t_vuelo:
    x = vx * t
    y = vy * t - 0.5 * g * t ** 2
    
    # Actualizar distancia máxima
    if x > x_max:
        x_max = x
    
    print(f"{t:10.2f}\t{x:.2f}\t{y:.2f}")
    
    t += dt

print(f"\nDistancia máxima alcanzada: {x_max:.2f} m")
