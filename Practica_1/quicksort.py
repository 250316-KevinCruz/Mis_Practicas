def quick_sort(lista):
    if len(lista) <=1:
        return lista
    pivote = lista[-1] #Tomamos el ultimo numero como pivote
    menores = [x for x in lista[:-1] if x <= pivote]
    mayores = [x for x in lista[:-1] if x > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayores)#se colocan los

numeros = [12,23,4,8,9]
print(quick_sort(numeros))#hace el llamado  a la funcion y se ejecuta en la lista