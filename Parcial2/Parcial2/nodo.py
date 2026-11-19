class Nodo:
    def _init_(self,dato):
        self.dato=dato
        self.siguiente=None

#Creacion de nodo individual
nodo_singular=Nodo("primer dato")
print(nodo_singular.dato)
print(nodo_singular.siguiente)