from collections import deque
import time

cola_pedidos = deque()

cola_pedidos.append("Pedido #101 - Café Americano")
cola_pedidos.append("Pedido #102 - Capuchino y Dona")
cola_pedidos.append("Pedido #103 - Té y Galleta de Avena")

print("Pedidos recibidos en la barra de la cafetería:")
for pedido in cola_pedidos:
    print(" -", pedido)

print("\nIniciando preparación y entrega de pedidos:")

while len(cola_pedidos) > 0:
    actual = cola_pedidos.popleft()

    print("\nPreparando y entregando:", actual)

    time.sleep(1)

    print("¡Pedido listo y entregado:", actual)
    print("(Pedidos restantes en la barra:", len(cola_pedidos), ")")

print("\nSe han entregado todos los pedidos. Barra despejada.")