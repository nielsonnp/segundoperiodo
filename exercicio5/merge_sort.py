

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

merge_sort(lista)

