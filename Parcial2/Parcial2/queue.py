from collections import deque
cola=deque()
#AGREGA ELEMENTOS A LA COLA(ENCOLAR)
cola.append("cliente 1")
cola.append("cliente 2")
cola.append("cliente 3")
#Sacar el primer elemento que lego (desencolar)
atentido=cola.popleft()
#Mostrar resultados obtenidos
print("Atendido: ",atentido)
print("cola restante",cola)