
#Selection Sort

lista = [1,45,10,35,100,13,147,500,80]

def selection_sort(lista):
    for i in range(0,len(lista)):
        for j in range(i+1,len(lista)):
            if lista[j] < lista[i]:
                min = lista[j];
                lista[j] = lista[i];
                lista[i] = min;

        print(i, lista)
        input()

selection_sort(lista)