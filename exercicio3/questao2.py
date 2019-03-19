'''2. Faça outro programa, incrementando o programa anterior da seguinte maneira: cada amigo
pode ter mais de um número de telefone, e estes números não podem mudar. Veja o exemplo:'''

dicionario = {}

while True:
    nome = input("Digite um nome: ")
    if nome == "-1":
        break
    telefones = []
    while True:
        telefone = input("Digite um número de telefone: ")
        if telefone == "-1":
            dicionario[nome] = telefones
            break
        telefones.append(telefone)

print(dicionario)