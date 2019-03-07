lista = []

def substitui(lista):
 for i in range(len(lista)):
   if (lista[i] > 0):
     lista[i] = 1
   else:
     lista[i] = 0
 print(lista)

for i in range(5):
 num = int(input("Digite um Número: "))
 lista.append(num)

substitui(lista)