maior_peso = 0
codigo_maior_peso = 0

maior_altura = 0
codigo_maior_altura = 0

contador = 0

soma_pesos = 0
soma_alturas = 0

codigo = int(input("Digite o código do cliente: "))

while (codigo != 0):
    altura = int(input("Digite a altura do cliente (em cm): "))
    peso = int(input("Digite o peso do cliente (em kg): "))

    if (altura > maior_altura):
        maior_altura = altura
        codigo_maior_altura = codigo

    if (peso > maior_peso):
        maior_peso = peso
        codigo_maior_peso = codigo

    contador += 1

    soma_alturas += altura
    soma_pesos += peso

    codigo = int(input("Digite o código do cliente: "))

print("Saiu!")

print("Cliente mais alto: ", codigo_maior_altura)
print("Cliente mais gordo: ", codigo_maior_peso)

print("Média das alturas: ", soma_alturas / contador)
print("Média dos pesos: ", soma_pesos / contador)