def presentar_usuario(nombre, rol="Invitado"):
    """Imprime el nombre del usuario y su rol."""
    print(f"Usuario: {nombre} | Rol: {rol}")
presentar_usuario("Ana")                 
presentar_usuario("Carlos", "Admin")     