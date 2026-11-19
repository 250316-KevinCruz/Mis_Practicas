from collections import deque
import time
cola_reproduccion=deque()
#AGREGA CANCIONES A LA COLA
cola_reproduccion.append("1. Antologia")
cola_reproduccion.append("2. Viento")
cola_reproduccion.append("3. Primera cita")
#MOSTRAR LAS CANCIONES EN ESPERA
print("CANCIONES EN ESPERA")
for cancion in cola_reproduccion:
    print("_",cancion)
    print("iniciando reproduccion")
#EL PRODUCTOR PROCESA LA COLA, CANCION POR CANCION
#DESENCOLAR
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    time.sleep(1) #simule la duracion del tema
    print(f"Finalizo:{cancion_actual}")
#MUESTRA CUNATAS CANCIONES QUEDAN EN LA COLA
print(f"Quedan:{len(cola_reproduccion)} canciones en la cola")
print("LA COLA DE REPRODUCCION HA FINALIZADO")