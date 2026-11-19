from collections import deque
import time
cola_turnos=deque()
#AGREGAR turnos a la cola

cola_turnos.append("-Turno A01 - Isidro Ortiz Ramirez")
cola_turnos.append("-Turno A02 - Guadalupe Lopez Días")
cola_turnos.append("-Turno A03 - Juana Lazcano Rodríguez")

#MOSTAR LAS CANCIOMES EN ESPERA
print("-----EJEMPLO 1-----")
print("Turnos emitidos en la fila del banco")
print("Personas en la cola ")
for clientes in cola_turnos:
    print("-",clientes)
print("  ")


#la cola empieza a repasar turno por turno para desencolar.
print("Inicializando atencion en ventanilla")
while cola_turnos:
    cola_actual=cola_turnos.popleft()
    print(f"Llamando a ventanilla: {cola_actual}")
    print(f"   Atencion finalizada: {cola_actual}")
    time.sleep(1) #simule la duracion del tema
    print(f"     (Clientes restantes:{len(cola_turnos)} )")
    print("")

#MUESTRA CUANTAS CANCIONES QUEDAN EN LA COLA 
print("  ")

print("Se han atendido todos los turnos. Fila Vacia  ")

print("--------------------------------------------------------------")
cola_hamburguesas=deque()
#AGREGAR turnos a la cola

cola_hamburguesas.append("-Turno B01 - Eshau Camaron Snachez")
cola_hamburguesas.append("-Turno B02 - Gael Torrez Samchez")
cola_hamburguesas.append("-Turno B03 - Eliel Ochoa Oso")

#MOSTAR LAS CANCIOMES EN ESPERA
print("-----EJEMPLO 2-----")
print("Turnos emitidos en el Mcdonals")
print("Personas en la cola ")
for clientes in cola_turnos:
    print("-",clientes)
print("  ")


#la cola empieza a repasar turno por turno para desencolar.
print("Inicializando atencion en ventanilla de comida rapida")
while cola_hamburguesas:
    cola_actuall=cola_hamburguesas.popleft()
    print(f"Vamos arecibir el pedido de : {cola_actuall}")
    print(f"   Comida recibida: {cola_actuall}")
    time.sleep(1) #simule la duracion del tema
    print(f"     (Clientes restantes en el Mcdonals:{len(cola_hamburguesas)} )")
    print("")

#MUESTRA CUANTAS CANCIONES QUEDAN EN LA COLA 
print("  ")

print("Se han atendido todos los turnos. Local Vacio  ")
