
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

lista = [30, 50, 10, 35, 70, 45, 80, 100, 22]

def bubblesort(lista):
    for i in range(1, len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

        print(i, lista)
        input()

bubblesort(lista)

