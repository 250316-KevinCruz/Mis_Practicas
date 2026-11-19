# Ejemplo de 3 funciones con parámetros en Python

# 1. Función para saludar a una persona
def saludar(nombre):
    """Recibe un nombre y muestra un saludo."""
    if not isinstance(nombre, str) or not nombre.strip():
        print("Error: El nombre debe ser un texto no vacío.")
        return
    print(f"Hola, {nombre}!")

# 2. Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    try:
        base = float(base)
        altura = float(altura)
        if base <= 0 or altura <= 0:
            raise ValueError("Las dimensiones deben ser positivas.")
        return base * altura
    except ValueError as e:
        print(f"Error: {e}")
        return None

# 3. Función para sumar una lista de números
def sumar_lista(numeros):
    """Suma todos los elementos de una lista de números."""
    if not all(isinstance(n, (int, float)) for n in numeros):
        print("Error: Todos los elementos deben ser números.")
        return None
    return sum(numeros)