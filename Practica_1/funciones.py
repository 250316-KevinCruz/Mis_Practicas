import detetime
def saludar():
    print("Hola, bienvenidos")
saludar()

def mostrar_hora():
    hora_actual=detetime.datetime.now().strftime("%H:M:S")
    print(f"La hora actual es:{hora_actual}")
mostrar_hora()