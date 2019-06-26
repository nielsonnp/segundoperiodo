
#Insert Sort


lista = [54,26,93,17,77,31,44,55,20]

def insertion_sort(lista):
    for i in range(1,len(lista)):
        x = lista[i]
        j = i-1
        while j > 0 and lista[j-1] > x:
            lista[j] = lista[j-1]
            j = j-1
            lista[j] = x

        print("Passo", i, lista)
        input()

insertion_sort(lista)
