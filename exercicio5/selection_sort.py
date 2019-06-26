
#Selection Sort

'''
array = [1,45,10,35,100,13,147,500,80]
size = len(array)


for i in range(0,size):
    for j in range(i+1,size):
        if array[j] < array[i]:
            min = array[j];
            array[j] = array[i];
            array[i] = min;



print(array)'''

lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]

def selection_sort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        t = lista[i]
        lista[i] = lista[menor]
        lista[menor] = t

        print("Passo", i, lista)
        input()

selection_sort(lista)