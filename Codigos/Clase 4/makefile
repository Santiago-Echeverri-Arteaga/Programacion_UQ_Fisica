# Variables
VENV := myenv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
RUTA := $(VENV)/bin/activate
LINT := pylint
CODIGO := main.py

# Crear el entorno virtual
entorno:
	python3 -m venv $(VENV)
	@echo "Entorno virtual creado en $(VENV)"

activar:
	. $(RUTA)
	@echo "Entorno $(VENV) activado"

# Instalar dependencias
install: entorno activar
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Dependencias instaladas"

# Crear archivos básicos
init:
	echo "# Proyecto en Python" > README.md
	echo "myenv/" > .gitignore
	$(PIP) freeze > requirements.txt
	@echo "Archivos README.md, .gitignore y requirements.txt creados"

# Ejecutar Linting
lint:
	$(LINT) --disable=R,C $(CODIGO)

# Limpiar el entorno
clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	@echo "Entorno virtual y archivos de caché eliminados"

# Crear todo
setup: entorno activar init install
	@echo "Proyecto configurado y listo para trabajar"

# Correr el código
run: 
	$(PYTHON) $(CODIGO)
