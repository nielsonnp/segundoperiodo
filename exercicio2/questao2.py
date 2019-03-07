'''2 - Faça um Programa que leia nomes completos de alunos da turma e exiba mensagens informando:
Quantos e quais alunos têm o sobrenome Silva;
Quantos e quais alunos têm mais de quatro palavras compondo seu nome completo;
Quantos e quais alunos têm as palavras “de” ou “da” no seu nome.
'''

lista = []

entrada = input("Digite seu nome completo: ")

while True:
    quebrar = entrada.split()
    lista.append(quebrar)
    entrada = input("Digite seu nome completo: ")
    if entrada == "-1":
        break

    silva = 0

for i in range(len(lista)):
    if ("silva" in lista[i]):
       silva += 1


print("Existem {} sobrenomes silva" .format(silva))
