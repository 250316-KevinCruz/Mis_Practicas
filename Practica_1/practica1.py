inventario_tech= ["laptop","tarjeta de video","procesador","memoria RAM"]
inventario_tech.append("disco SSD")

inventario_tech.insert(3,"fuente de poder")

inventario_tech.extend(["Gabinete","monitor 4k","teclado mecanico","mouse gamer"])
print(inventario_tech)
posicion= inventario_tech.index("monitor 4k")
print("La posicion que tienen el objeto es", posicion)
inventario_tech[3] = "memoria RAM DDR5"

#Eliminar Datos
equipo_despachado=inventario_tech.pop()
inventario_tech.remove("tarjeta de video")
print ("El equipo ya vendido es. ",equipo_despachado)
print("el numero de productos que quedan son:",len(inventario_tech))


