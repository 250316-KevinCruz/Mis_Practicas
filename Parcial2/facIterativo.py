def factor_iterativo(n):
    resultado=1
    for i in range(1, n+1):
        resultado=resultado*i
    return resultado
    print (factor_iterativo(5))