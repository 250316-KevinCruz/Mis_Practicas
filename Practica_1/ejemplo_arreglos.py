import heapq
import numpy as np


def dijkstra_numpy(matriz_adyacencia, inicio):
    """Calcula la distancia más corta desde un nodo de inicio usando matrices de NumPy.

    - matriz_adyacencia: Arreglo 2D donde matriz[i][j] representa el peso de la
    arista.
    """
    num_nodos = matriz_adyacencia.shape[0]

    # Inicializar distancias a infinito usando arreglos de NumPy
    distancias = np.full(num_nodos, np.inf)
    distancias[inicio] = 0

    # Cola de prioridad estructurada como tupla: (distancia, nodo)
    cola_prioridad = [(0, inicio)]
    visitados = np.zeros(num_nodos, dtype=bool)

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if visitados[nodo_actual]:
            continue
        visitados[nodo_actual] = True

        # Obtener vecinos usando filtrado dinámico de NumPy (pesos mayores a 0)
        (vecinos,) = np.where(matriz_adyacencia[nodo_actual] > 0)

        for vecino in vecinos:
            peso = matriz_adyacencia[nodo_actual, vecino]
            nueva_distancia = distancia_actual + peso

            # Si encontramos un camino más corto hacia el vecino, actualizamos
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancias


# --- PRUEBA DEL ALGORITMO AVANZADO ---

# Matriz de adyacencia de 5x5 (0 significa que no hay conexión directa)
grafo = np.array()

nodo_origen = 0
resultado = dijkstra_numpy(grafo, nodo_origen)

# Impresión indexada de los resultados
print("\n--- Resultados de Dijkstra ---")
for nodo, distancia in enumerate(resultado):
    print(
        f"Distancia mínima desde Nodo {nodo_origen} al Nodo {nodo}: {distancia}"
    )
