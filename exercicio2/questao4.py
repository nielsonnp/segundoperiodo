'''4. Faça um programa que tenha uma classe que define uma Pessoa, com atributos nome, idade e
sexo. Em seguida, o programa deve ser capaz de ler os mesmos dados e imprimir a confirmação dos
dados criados, que estarão armazenados em uma estrutura de dados. Estabeleça um critério de
parada.'''

class Pessoa:

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __repr__(self):
        return "Nome: {}, Idade: {}, Sexo: {} " .format(self.nome, self.idade, self.sexo)

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_sexo(self):
        return self.sexo

lista = []

while True:

    nome = input("Digite seu nome: ")

    if nome == "-1":
        break

    idade = int(input("Digite sua idade: "))

    sexo = input(("Digite seu sexo: "))

    pes = Pessoa(nome, idade, sexo)
    lista.append(pes)

print(lista)



