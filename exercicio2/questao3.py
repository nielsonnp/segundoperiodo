
notas = []
aprovado = 0
reprovado = 0

print('Digite notas de 0 - 100:')

for i in range(0,10):
    nome = input("Qual o seu Nome? ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1+n2+n3)/3
    notas.append([nome,media])
    if (media >= 70):
        aprovado += 1
    else:
        reprovado += 1

print("Números de alunos com média maior ou igual a 70 = {}" .format(aprovado))
print("Nome dos alunos e médias {}".format(notas))