<div align="center">
<h1>Programación</h1>

<img src="https://www.nextibs.com/wp-content/uploads/2021/12/seguridad-informatica-2048x877.jpeg.webp" alt="Imagen con una pantalla digital y una mano acercansose a tocarla"
     width="768"
     height="329">
</div>

**Programa de Física**
**Universidad del Quindío**

**Docente:** *Ph.D. Santiago Echeverri Arteaga*

# Curso de Programación en Python para Físicos

## Descripción del Curso
La asignatura se centrará en la aplicación de Python a problemas de la física y la ciencia de datos, con un enfoque en proyectos prácticos. Los estudiantes aprenderán programación orientada a objetos desde el inicio, junto con el uso de bibliotecas científicas y herramientas de manejo de datos.

## Objetivos del Curso
1. Introducir a los estudiantes en la programación orientada a objetos con Python.
2. Desarrollar habilidades en el uso de bibliotecas científicas como NumPy, SciPy, y Matplotlib.
3. Enseñar técnicas de manejo y análisis de datos utilizando Pandas.
4. Aplicar conocimientos de programación y bases de datos a proyectos prácticos.
5. Capacitar a los estudiantes en el uso de herramientas y métodos de la ciencia de datos.

Recuerde que para el curso deberá tener instalado los [**compiladores de Python**](https://www.python.org/downloads/), [**Visual Studio Code**](https://code.visualstudio.com/download) y el [**GIT BASH**](https://git-scm.com/downloads). Si desea complementar el contenido dado en el aula de clase, puede revisar el siguiente material audiovisual concerniente al manejo de VSCode y Git:

1. [VSCode](https://youtu.be/Ei1y51K8jQk)
2. [Git Tutorial *Hola Mundo*](https://youtu.be/VdGzPZ31ts8)
3. [Git Tutorial *codigofacilito*](https://www.youtube.com/watch?v=zH3I1DZNovk&list=PL9xYXqvLX2kMUrXTvDY6GI2hgacfy0rId)
4. [Documental Hola Mundo!](https://www.youtube.com/watch?v=GNRhblNcZv4)

Ya teniendo instalado lo anterior, descargue el archivo requirements.txt del presente repositorio, cree un entorno virtual de Python y en una terminal (de GIT BASH si está en Windows)  copie el siguiente código

```bash
pip install requirements.txt
```

## Esquema del Curso

### Semana 1: Introducción y Contextualización
**Clase 1:**
- Introducción al curso, objetivos y metodología.
- Revisión del sílabo y expectativas.
- Instalación y configuración del entorno de desarrollo (Python, Anaconda, Jupyter Notebooks).

**Clase 2:**
FESTIVO

**Clase 3:**
- Fundamentos de Git y GitHub.
- Creación de un entorno virtual de Python e instalación de Jupyter
- Archivos README.md requirements.txt y .gitignore en un repositorio.
- Creación de un repositorio, commits.


### Semana 2: Fundamentos de Programación en Python
**Clase 4:**
- Continuación con Git y GitHub.
- Ramas
- Colaboración en proyectos: Pull requests y manejo de conflictos.
- Introducción a Python: sintaxis básica.
- `print()` y `input()`.
- Tipos de datos básicos: enteros, flotantes, cadenas, y booleanos.
- Tarea: Creación de un repositorio que contenga un programa simple de entrada y salida.

**Clase 5:**
- Variables y operadores.
- Estructuras de control: condicionales (`if`, `elif`, `else`).
- Estructuras de control: ciclos (`for`, `while`).
- Ejercicio práctico: Programas con decisiones y bucles.

**Clase 6:**
- Listas, tuplas, diccionarios y conjuntos.
- Operaciones básicas con colecciones.
- Ejercicio práctico: Manipulación de colecciones.


### Semana 3: Fundamentos de Programación Orientada a Objetos (POO)
**Clase 7:**
- Introducción a la programación orientada a objetos.
- Conceptos de clases y objetos.
- Introducción a los métodos mágicos
- Atributos y métodos
- Ejemplos básicos en Python.

**Clase 8:**
- Revisión de códigos de ejemplo
- introducción a métodos numéricos



**Clase 9:**
- Trabajo individual asistido: Crear una clase aplicada a la física con:
     - Constructor  `__init__`
     - Uso de cadenas, números (`int`/`float`)
     - Implementar los métodos `__add__` `__sub__` `__mul__` `__rmul__` `__call__` `__setitem__` `__getitem__` `__str__`
     - Algún método adicional
     - Implementar algún método numérico diferente de los ejemplos de clase y que involucre ciclos/condicionales
     - Implementar dos o más métodos mágicos adicionales

### Semana 4: Fundamentos de Programación en Python
**Clase 10:**
- Trabajo autónomo en la tarea

**Clase 11:**
- Exposiciones y revisión de trabajo autónomo

**Clase 12:**
- Introducción a Matplotlib Orientado a Objetos


### Semana 5: Matplotlib y Funciones
**Clase 13:**
- Matplotlib orientado a Objetos

**Clase 14:**
- Funciones en Python: definición y llamada.
- Argumentos y parámetros.
- Alcance de las variables.
- Ejercicio práctico: Creación y uso de funciones.

**Clase 15:**
- Trabajo asistido: Crear funciones y métodos implementado funciones
     - Crear atributos en una clase con figures y Axes
     - Hacer uso de *args y **kwargs
     - Crear métodos para hacer gráficas y animaciones
- **Tarea Matplotlib:** Implementar un método para hacer una grafica en matplotlib. Realizar una animación (gif) usando matplotlib.

### Semana 6: Geradores y decoradores

**Clase 16:**
- Trabajo individual: Preparar exposición de Numpy, Scipy o Simpy en grupos.

**Clase 17:**
- Generadores
- Comprensión de generadores, de listas y de diccionarios

**Clase 18:**
- Exposición tarea Matplotlib
- Lambdas, Zip, Map, Enumerate.
- Decoradores.

### Semana 7: Funciones y recursividad

**Clase 19:**  
- Ejemplos de generadores
- Recursividad
- Ejemplos recursividad

**Clase 20:**
- Break, continue, for-else
- Herencia
- **Tarea:** Implementar un método numérico SIN hacer uso de librerías diferentes a `math` en donde haga uso de recursividad o de ciclos `for` anidados.

**Clase 21:**
- Herencia múltiple
- Encapsulación
- Manejos de excepciones
- Getters y Setters
- Atributos y métodos privados
- Métodos de clase, métodos de instancia y métodos estáticos
- Ejemplos encapsulación y herencia múltiple
- Abstracción
- Creación de clases abstractas

### Semana 8: Modulos

**Clase 22:**
- Exposición librerías `os` y `sys` con ejemplos de uso
- Polimorfismo
- Ejemplos de Polimorfismo

**Clase 23:**
- Módulos y paquetes.
- Importación y uso de módulos estándar.
- Ejercicio práctico: Creación y uso de módulos personalizados.

**Clase 24:**
- Trabajo indeopendiente

### Semana 9: Introducción a manejo de datos

**Clase 25:**
- Exposiciones de Numpy, Scipy y Simpy
- Exposición tareas
- Tarea: Crear una librería con 
  - `__init__.py`
  - Clases con uso de Matplotlib
  - Uso de generadores y comprensión
  - Uso de decoradores de manera no trivial
  - Definición de funciones con implementación de un método numérico
  - Uso de *args y **kwargs en Python
- Importación de datos con Python, Numpy

**Clase 26:**
- Introducción a bases de datos
- SQL, ORM y NoSQL

## [Bibliografía Recomendada](https://1drv.ms/u/s!AvgPrG5g0hS9geYeVJN97X8LEwTkiQ?e=f4NW5x).
