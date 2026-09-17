#recorrido de >Lista 1
#lista=[10,20,30,40,50,60]
#for i in range (len(lista)):
    #Asi se hacen los cilos en python 
    #print(lista[i])
    #print (lista[2])
    #print (lista [-1])
    #print( lista[1:5])
    #print (lista[:3]) Pone toda la lista y solamente la posicion 3 es la que no se imprime 
    #print (lista[::]) Imprime absolutamente todos los terminos normales 
    #print (lista[::-1]) Empieza a imprimir desde el ultimo termino hasta la del comienzo 
    #cadena="¡Hola, Python!"
    #"print(cadena[0:5])
lista = [29,10,14,100]
n = len(lista)
swapped = True 
while swapped:
    swapped = False
for i in range (n-1):
    if lista[i]>lista[i+1]:
        lista[i],lista[i+1]=lista[i+1],lista[i]
        swapped=True
print ("Lista ordenada.",lista)