def factorial_iterativo(n):
    resultado=1
    for i in range(1,n+1):
        resultado=resultado*i
    return resultado
print(factorial_iterativo(5))