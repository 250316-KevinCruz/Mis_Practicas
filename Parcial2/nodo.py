class Nodo:
    def _init_(self,dato):
        self.dato=dato
        self.siguiente=None

#Creacion  de nodos individuales

nodo_singular=Nodo("Primer Dato")
print(nodo_singular.dato)
print(nodo_singular.siguiente)