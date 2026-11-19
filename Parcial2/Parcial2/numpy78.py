import numpy as np
#DEFINICION DE MATRICES
A= np.array([[1,2],[3,4]])
B= np.array([[5,6],[7,8]])
#SUMA ELEMENTO A AELEMENTO
suma= A+B
print("..SUMA(A+B)..")
print(suma)
#MULTIPLICACION
prod_elem=A*B
print("..MULTIPLICACION(AXB)..")
print(prod_elem)
#PRODUCTO MATRICIAL
prod_mat=A@B
print("..PRODUCTO MATRICIAL(A@B)..")
print(prod_mat)
#TRANSPUESTA
transpuesta=A.T
print("..TRANSPUESTA DE A.T ..")
print(transpuesta)
#DETERMINANTE E INVERSA
det=np.linalg.det(A)
inv=np.linalg.det(B)
print("..DETERMINANTE DE A ..")
print(det)
print("..DETERMINANTE DE B ..")
print(inv)