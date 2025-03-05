a = 10
b = 0
try:
    a/b
except ZeroDivisionError as e:
    raise ValueError(f"Se presentó el siguiente fallo {e}, debido a que se intentó dividir la presión entre la temperatura y P={a}, T={b}")

