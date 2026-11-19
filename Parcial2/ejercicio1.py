def limpiar_feed(publicaciones):
    if len(publicaciones) <= 1:
        return publicaciones    
    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    else:
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])
resultado = limpiar_feed(["Post A", "Post B", "Post ", "Post C", "Post B"])
print(resultado)

#ejercicio 2
def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    if not depositos:
        return 0.0
    
    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)

resultado = calcular_saldo_final([1000, 2000, 1500], 0.05)
print(resultado) .. 

# ejercicio 3
def maxima_profundidad(comentarios: list) -> int:

    if not comentarios:
        return 0
    
    max_prof = 0
    for elem in comentarios:
        if isinstance(elem, list):
            prof = 1 + maxima_profundidad(elem)
        else:
            prof = 1
        if prof > max_prof:
            max_prof = prof
            
    return max_prof

hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
print(maxima_profundidad(hilo))