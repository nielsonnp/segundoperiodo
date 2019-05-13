
#Insert Sort

lista = [30, 50, 10, 35, 70, 45, 80, 100, 22]

def insertionSort(lista):
    for i in range(1,len(lista)):
        x = lista[i]
        j = i-1
        while j>=0 and x<lista[j]:
            lista[j+1] = lista[j]
            j=j-1
        lista[j+1] = x


insertionSort(lista)
print(lista)