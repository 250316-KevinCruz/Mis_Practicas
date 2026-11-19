def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print (factorial(5))


#Con potencia
def potencia (base,exponente):
    if exponente==0:
        return 1
    else:
        return base*potencia (base, exponente-1)
print (potencia(2,4))