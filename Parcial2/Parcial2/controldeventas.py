import numpy as np
A= np.array([[10,15],[20,5]])
B= np.array([[5,12],[15,8]])

totalProductos= A+B
print("Total de productos vendidos(Sabado + Domingo)")
print(totalProductos)

precio=50
ingresoTotal= totalProductos*precio
print("Ingreso total en pesos(a 50 pesos por producto)")
print(ingresoTotal)