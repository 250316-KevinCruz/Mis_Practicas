#CREACION DE UNA MATRIZ
matriz=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#ACCESO A ELEMENTOS
print(matriz[1][2])#imprime indice 1 columna indice 2

#MODIFICAR ELEMENTO
matriz[0][0]=50

#RECORRER LA MATRIZ
for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")
        print()