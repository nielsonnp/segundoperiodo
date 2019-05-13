'''1. De acordo com os exemplos vistos em sala, faça um programa que receba do usuário
dados para compor uma lista de Anúncios que serão exibidos em um site. Cada anúncio tem
o tempo, em segundos, a frase a ser exibida, e a empresa responsável.  Após isso, você
deve imprimir uma lista ordenada dos anúncios, considerando um dos itens para ordenar.
Você pode ordenar pelo tempo, pelo nome da empresa ou pelo tamanho da frase.'''

class Anuncio:
    def __init__(self, empresa, tempo, frase):
        self.empresa = empresa
        self.tempo = tempo
        self.frase = frase

    def __repr__(self):
        return "Empresa {0} , Tempo {1}, Frase {2} ".format(self.empresa, self.tempo, self.frase)


    def getEmpresa(self):
        return self.empresa

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getTempo(self):
        return self.tempo

    def setTempo(self, tempo):
        self.tempo = tempo

    def getFrase(self):
        return self.frase

    def setFrase(self, frase):
        self.frase = frase

lista = []
contador = 0

empresa = input("Digite a empresa do anúncio: ")

while (empresa != '-1'):

    tempo = int(input("Digite o tempo do anúncio: "))
    frase = input("Digite a frase do anúncio: ")
    nome = Anuncio(empresa, tempo, frase)
    lista.append(nome)

    if nome == True:
        contador += 1

    empresa = input("Digite a empresa do anúncio: ")

print("Saiu!")

lista.sort(key=lambda a:a.tempo)
print(lista)