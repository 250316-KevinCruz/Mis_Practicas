def maxima_profundidad(comentarios):
    if comentarios==[]:
        return 0
    else:
        profundidad_maxima = 0
        for elemento in comentarios:
            if isinstance(elemento, list):
                profundidad = 1 + maxima_profundidad(elemento)
            else:
                profundidad = 1
            if profundidad > profundidad_maxima:
                    profundidad_maxima = profundidad
        return profundidad_maxima
    
hilo=["Comentario 1",["Respuesta 1.1",["Respuesta 1.1.1"]], "Comentario 2"]

resultado = maxima_profundidad(hilo)

print("La profundidad maxima del hilo es", resultado)