'''Questa1 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.'''

lista = []

texto = input("Digite 10 caracteres: ")
lista.append(texto)

vogais = 0
consoantes = 0

for caracter in texto:

    if caracter in 'aeiou':
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1

print ("Consoantes: {}" .format(consoantes))

