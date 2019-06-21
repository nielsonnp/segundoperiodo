
class Fila:
    def __init__(self):
        self.fila = []

    def tamanho(self):
        return len(self.fila)

    def entrar(self, pessoa):
        self.fila.append(pessoa)

    def primeiro(self):
        if (self.vazio() == False):
            return self.fila[0]
        else:
            return None

    def ultimo(self):
        if (self.vazio() == False):
            return self.fila[len(self.fila) -1]
        else:
            return None

    def sair(self):
        if (self.vazio() == False):
            return self.fila.pop(0)

    def vazio(self):
        if (len(self.fila) == 0):
            return True
        else:
            return False

class Hospital:
    def __init__(self):
        self.gestantes = Fila()
        self.idosos = Fila()
        self.demais = Fila()

    def entrar_na_fila(self, nome, idade, eh_gestante):
        if (eh_gestante == "Sim"):
            self.gestantes.entrar(nome)
        elif (idade > 60):
            self.idosos.entrar(nome)
        else:
            self.demais.entrar(nome)

    def ordem_atendimento(self):
        for i in range (self.gestantes.tamanho()):
            print(self.gestantes.primeiro())
            self.gestantes.sair()

        for i in range (self.idosos.tamanho()):
            print(self.idosos.primeiro())
            self.idosos.sair()

        for i in range (self.demais.tamanho()):
            print(self.demais.primeiro())
            self.demais.sair()


hosp = Hospital()

while True:

    nome = input('Digite seu nome: ')

    if nome == "-1":
        break

    idade = int(input("Digite a Idade: "))
    gestante = input("É gestante? ")


    hosp.entrar_na_fila(nome, idade, gestante)


print("Saiu!")
print("Ordem de Atendimento: ")


hosp.ordem_atendimento()






