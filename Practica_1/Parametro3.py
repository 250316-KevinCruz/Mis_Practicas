def calcular_promedio(*calificaciones):
    """Calcula el promedio de una cantidad variable de números."""
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

print(calcular_promedio(8, 9, 10))       
print(calcular_promedio(7.5, 9.2))     