
def calcular_saldo_final(depositos, tasa_interes):
    if depositos == []:
        return 0.0
    else:
        saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
        saldo_nuevo = (saldo_anterior + depositos[-1]) * (1 + tasa_interes)
        print("Año", len(depositos), ": (", saldo_anterior, "+", depositos[-1], ") *", (1 + tasa_interes), "=", saldo_nuevo)
        return saldo_nuevo

depositos = [1000, 2000, 1500]
tasa_interes = 0.05

resultado = calcular_saldo_final(depositos, tasa_interes)

print("Resultado final:", resultado)
