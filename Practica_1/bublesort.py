#lista=[5,10,24,100]
#n = len(lista)
#swapped = True
#while swapped:
    #swapped=False
#for i in range(n-1):
    #if lista[i]>lista[i+1]:
        #lista[i],lista[i+1]=lista[i+1],lista[i]
        #swapped=True
#print("lista ordenada:",lista)

lista=[4,2,6,8,5,7]
print(lista)
for i in range(len(lista)):
    for x in range(len(lista)-1):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
            print(lista)