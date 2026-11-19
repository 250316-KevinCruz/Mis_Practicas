frutas=[]
frutas.append("manzana")
frutas.append("pera")
frutas.append("naranja")
frutas.append("fresa")
frutas.append("mango")
frutas.append("guayaba")
frutas.append("kiwi")
frutas.append("papaya")
frutas.append("mandarina")
frutas.append("manzana")

#OPERACION TOP PEEK
fruta_actual=frutas[-1]
print("fruta actual en la pantalla:",fruta_actual)

#OPERACION PARA DESAPILAR (POP)
for i in range(4):
    eliminar = frutas.pop()
print("Fruta eliminada: ",eliminar)
print("historial despues de presionar 'atras'",frutas)


#OPERACION TAMAÑO (SIZE)
total_frutas= len(frutas)
print("paginas previas guardadas",total_frutas)

#OPERACION VACIA (EMPTY)
sin_frutas=len(frutas)==0
print("¿El historial esta vacio?",sin_frutas)

vacio=len(frutas)==0
print("¿El historial esta vacio?",sin_frutas)
while len(frutas) > 0:
    estado=frutas.pop()
    print("eliminado:",estado)
vacio=len(frutas)==0
print("¿El historial esta vacio?",sin_frutas)


