'''1. Faça um Programa que leia nomes dos seus amigos e os números de telefones de cada um
deles. Para sair do programa, siga o exemplo: '''

dicionario = {}

while True:
    nome = input("Digite o nome: ")
    if nome == "-1":
        break

    telefone = int(input("Digite o número de telefone: "))

    dicionario[nome] = telefone

print(dicionario)