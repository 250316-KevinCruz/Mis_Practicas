class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente= None

class ListaEnlazada:
    def __init__(self):
        self.cabeza=None #Referencia inicial que va a indicar el origen

    def insertar_final(self,dato):
        nuevo_nodo=Nodo(dato)
#CASO 1: si la lista esta vacia
        if self.cabeza is None:
            self.cabeza=nuevo_nodo
            return
#CASO 2 recorrer hasta el ultimo nodo que existe
        actual=self.cabeza
        while actual.siguiente is not None:
            actual=actual.siguiente

#Conectar el ultimo nodo con el nuevo nodo
        actual.siguiente=nuevo_nodo
    def mostrar_lista(self):
        actual=self.cabeza
        elementos=[]

        while actual is not None:
            elementos.append(str(actual.dato))
            actual=actual.siguiente
        print("...".join(elementos)+"--None")

#USO DEL PROGRAMA
lista=ListaEnlazada()
#insertar elementos a utilizar
lista.insertar_final("A")
lista.insertar_final("B")
lista.insertar_final("C")

lista.mostrar_lista()