import matplotlib.pyplot as plt

datos = [42, 12, 88, 23, 7, 65, 34, 50]

def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if a[j] > clave:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = clave
    return a, comp


def seleccion(arr):
    a = arr.copy()
    comp = 0
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, comp

# Ejecutamos los dos algoritmos
lista_ordenada, comp_ins = insercion(datos)
_, comp_sel = seleccion(datos)

# Graficación con matplotlib
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# Gráfico 1 Lista Desordenada
ax1.bar(range(len(datos)), datos, color='red')
ax1.set_title('1. LISTA ORIGINAL')
ax1.set_ylabel('Valor')

# Gráfico 2 Lista Ordenada
ax2.bar(range(len(lista_ordenada)), lista_ordenada, color='blue')
ax2.set_title('2. LISTA ORDENADA')

# Gráfico 3 Comparaciones realizadas
ax3.bar(['Inserción', 'Selección'], [comp_ins, comp_sel], color=["#175b8b", "#FF4500"])
ax3.set_title('3. COMPARACIONES')
ax3.set_ylabel('Cantidad')

plt.tight_layout()
plt.show()