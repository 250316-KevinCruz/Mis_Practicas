calificaciones =[ 1,0,9.5,2,8,3,7,4,7,6,5,10,9,8,4.6,8]
n =len(calificaciones)
swapped =True
while swapped:
    swapped = False
    for i in range (n-1):
        print(f"{i+1} Recorrido (i={i})")
        if calificaciones[i]<calificaciones[i+1]:
            print ("i= ",i)
            calificaciones[i],calificaciones[i+1]=calificaciones[i+1],calificaciones [i]
            swapped=True
            print (calificaciones)
print("orden descendente: ",calificaciones)
swapped=True
while swapped:
    swapped =False
    for i in range (n-1):
        print(f"{i+1} Recorrido (i={i})")
        if calificaciones[i]>calificaciones[i+1]:
            print ("i= ",i)
            calificaciones[i],calificaciones[i+1]=calificaciones [i+1],calificaciones[i]
            swapped=True
            print (calificaciones)
print ("Orden ascendentes: ",calificaciones)



