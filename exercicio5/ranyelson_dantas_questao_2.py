
'''
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

bubble_sort(lista)'''

'''
# B) Selection Sort

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

selection_sort(lista)'''

'''
# C) Insertion Sort

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

insertion_sort(lista)'''

'''
# D) Merge Sort

lista = [54,26,93,17,77,31,44,55,20]

def merge_sort(lista):
    if len(lista) > 1:
        middle = len(lista) // 2
        left = lista[:middle]
        right = lista[middle:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left [i] < right[j]:
                lista[k] = left[i]
                i = i + 1
            else:
                lista[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            lista[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            lista[k] = right[j]
            j = j + 1
            k = k + 1

        print(lista)
        input()

merge_sort(lista)'''