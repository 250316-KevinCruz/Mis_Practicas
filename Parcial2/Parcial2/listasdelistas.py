A = [[10, 15], [20, 5]]
B = [[5, 12], [15, 8]]

total_productos = [[A[i][j] + B[i][j] for j in range(len(A[0]))]for i in range(len(A))]

precio = 50
ingreso_total = [[total_productos[i][j] * precio for j in range(len(total_productos[0]))]
        for i in range(len(total_productos))]

print("Total de productos vendidos (Sábado + Domingo):")
for fila in total_productos:
    print(fila)

print("Ingreso total en pesos (a 50 pesos por producto):")
for fila in ingreso_total:
    print(fila)