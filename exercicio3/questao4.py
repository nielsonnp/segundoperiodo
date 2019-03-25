'''4. Faça um programa que tenha uma classe que define um Aluno do IFPB, com atributos nome,
idade, matricula. Você deve prover uma forma de armazenar as disciplinas, referenciadas pelo
seu nome, que terão suas notas. Deve existir uma função que retorne a média de uma disciplina,
tratando o caso de não haver essa disciplina cadastrada.'''

class Aluno:

    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula


    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_matricula(self):
        return self.matricula


aluno1 = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
matricula = input("Digite sua mátricula: ")

print("==========================================================")
cadastro = Aluno(aluno1, idade, matricula)
print("Nome do Aluno: {} - Idade: {} - Mátricula: {} "
      .format(cadastro.nome, cadastro.idade, cadastro.matricula))

print("==========================================================")

disciplinas = {"Português":[9.0,8.0], "Matemática":[10.0, 8.0],
               "Estrutura de Dados":[9.0,10.0]}

print("Disciplinas e notas cadastradas: \n {}".format(disciplinas))

print("==========================================================")

for nome in disciplinas:
    media = sum(disciplinas[nome])/len(disciplinas[nome])
    print("Média em {}: {} ".format(nome,media))

print("==========================================================")


