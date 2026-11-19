from collections import deque
import time

cola_turnos = deque()

cola_turnos.append("Turno A01 - ISIDRO ORTIZ RAMIREZ")
cola_turnos.append("Turno A02 - GUADALUPE PEREZ DIAZ")
cola_turnos.append("Turno A03 - JUANA LAZCANO RODRIGUEZ")

print("Turnos emitidos en la fila del banco:")
for turno in cola_turnos:
    print(" -", turno)

print("\nIniciando atención en ventanilla")

while len(cola_turnos) > 0:
    cliente = cola_turnos.popleft()

    print("\nLlamando a ventanilla:", cliente)

    time.sleep(1)

    print("Atención finalizada:", cliente)
    print("(Clientes restantes en la fila:", len(cola_turnos), ")")

print("\nSe han atendido todos los turnos. Fila vacía.")