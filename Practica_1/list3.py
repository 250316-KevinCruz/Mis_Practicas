frutas= ["manzana","guayaba","uva"]
#Actualizar
frutas[1] = "pera"
print(frutas)

#Inserta nuevos elementos
frutas.append("sandia")
print(frutas)

#Agrega multiples elemnetos al final
frutas.extend(["kiwi","Mango"])
print(frutas)

#Eliminar
retirado= frutas.pop(2)
print(frutas)

#Elimina el ultimo valor de la lista
ultimo=frutas.pop()
print(frutas)

#Busca y Elimina un termino en especifico 
frutas.remove("sandia")
print(frutas)

#del utiliza palabras clave para borrar una casiilla directamente 
del frutas[0]
posicion= frutas.index("kiwi")
print(frutas)