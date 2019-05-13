#Exemplo da apostila algoritimos de ordenação

'''lista = []

contador_idosos = 0

idoso = input("Você é maior de 65 anos? S/N...")

while (idoso != '-1'):
    if idoso == 'S':
        lista.append(True)
        contador_idosos =+ 1

    elif (idoso == 'N'):
        lista.append(False)

    idoso = input("Você é maior de 65 anos? S/N...")

lista.sort(reverse=True)
print(lista)'''

class Paciente:
    def __init__(self, nome, idade, documento):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def __repr__(self):
        return 'Pessoa {0}, {1} anos, documentos {2}'.format(self.nome, self.idade, self.documento)

    def idoso(self):
        if self.idade > 65:
            return True
        return False

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_documento(self):
        return self.documento

    def set_documento(self, documento):
        self.documento = documento

lista_pacientes = []
contador = 0

nome = input("Digite seu nome: ")

while (nome != '-1'):
    idade = int(input("Digite sua idade: "))
    documento = int(input("Digite seu documento: "))
    pessoa = Paciente(nome, idade, documento)
    lista_pacientes.append(pessoa)

    if pessoa.idoso() == True:
        contador += 1

    nome = input("Digite seu nome: ")



lista_pacientes.sort(key=lambda a:a.documento)
print(lista_pacientes)





