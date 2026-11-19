historial_navegacion = []
#OPERACIONES APILAR PUSH
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.com")
print("Este es el historial de Navegacion: ", historial_navegacion)

#OPERACION CON PEEK
pagina_actual=historial_navegacion[-1]
print ("Pagina actual en pantalla",pagina_actual)

#OPERACION PARA DESAPILAR 
pagina_cerrada=historial_navegacion.pop
print("saliendo de: ",pagina_cerrada)
print("Historial de navegacion despues de presionar 'atras': ",historial_navegacion)

#OPERACION DE TAMAÑO(SIZE)
total_paginas=len(historial_navegacion)
#El len es para conntar cuantos elementos hay en la lista
print("Paginas previas guardadas",total_paginas)

#OPERACIONES VACIAS (EMPTY)
sin_paginas=len(historial_navegacion)==0
print("¿El historial de navegacion esta vacio",sin_paginas)