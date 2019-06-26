
#Exemplo Bubble Sort

'''
lista = [30, 50, 10, 35, 70, 45, 80, 100, 22]
tam_lista = len(lista)

# bubble sort
for i in range(tam_lista):
    troca = False
    for j in range(1, tam_lista - i):
        if lista[j] < lista[j - 1]:
            lista[j], lista[j - 1] = lista[j - 1], lista[j]
            troca = True
    if not troca:
        break

print(lista)'''



# A) bubble_sort

lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def bubble_sort(lista):
    for i in range(1, len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                a = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = a

        print("Passo", i, lista)

        input()

bubble_sort(lista)
