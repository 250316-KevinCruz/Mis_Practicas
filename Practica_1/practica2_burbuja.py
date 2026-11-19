calificaciones = [9.2,8.5,8.3,9.0,8.6,8.8,9.8,10.0,8.1,10.0,9.6,9.3,10.0,8.4,10.0]
n = len(calificaciones)
swapped = True
while swapped:
    swapped=False
for i in range(n-1):
    if calificaciones[i]>calificaciones[i+1]:
        calificaciones[i],calificaciones[i+1]=calificaciones[i+1],calificaciones[i]
        swapped=True
print("Orden Ascendente:",calificaciones)

#orden descendente
calificaciones = [9.2,8.5,8.3,9.0,8.6,8.8,9.8,10.0,8.1,10.0,9.6,9.3,10.0,8.4,10.0]
swapped = True
while swapped:
    swapped=False
for i in range(len(calificaciones)):
    for x in range(len(calificaciones)-1):
        if calificaciones[x]>calificaciones[x+1]:
            aux=calificaciones[x]
            calificaciones[x]=calificaciones[x+1]
            calificaciones[x+1]=aux
            print("Orden descendente:",calificaciones)