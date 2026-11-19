def burbuja(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista


def insercion(lista):
    a = lista.copy()
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


def seleccion(lista):
    a = lista.copy()
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


def quick_sort(lista):
    if len(lista) <=1:
        return lista
    pivote = lista[-1] #Tomamos el ultimo numero como pivote
    menores = [x for x in lista[:-1] if x <= pivote]
    mayores = [x for x in lista[:-1] if x > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayores)

numeros = [12,23,4,8,9]
print(quick_sort(numeros))


# Programa principal
def main():
    opcion = 0

    while opcion != 5:
        print("1. Burbuja")
        print("2. Selección")
        print("3. Inserción")
        print("4. Quick sort")
        print("5. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 5:
            print("Programa finalizado")

        elif opcion >= 1 and opcion <= 4:
            numeros = list(map(int, input(
                "Ingresa números separados por comas: "
            ).split(",")))

            if opcion == 1:
                resultado = burbuja(numeros.copy())
            elif opcion == 2:
                resultado = seleccion(numeros.copy())
            elif opcion == 3:
                resultado = insercion(numeros.copy())
            else:
                resultado = quick_sort(numeros.copy())

            print("Lista ordenada:", resultado)

        else:
            print("Opción no válida")


main()

