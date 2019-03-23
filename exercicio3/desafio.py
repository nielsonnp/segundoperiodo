class Tamagushi:

    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)


    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setFome(self, fome):
        self.fome = fome

    def getFome(self):
        return self.fome

    def setSaude(self, saude):
        self.saude = saude

    def getSaude(self):
        return self.saude

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def comer(self, fome):
        self.fome -= fome

    def tomarRemedio (self, saude):
        self.saude += saude

    def getHumor(self):
        return self.getSaude() - self.getFome()

#Variável com valores inicial
b = Tamagushi("Tamagushi", 100, 0, 5)

#Print de apresentação do Tamagushi
print("Olá, me chamo {} e tenho {} anos! ". format(b.nome,b.idade))

comida = int(input("Tamagushi, Quer comer quanto? Digite entre 0 - 100!\n"))

#Condicional para não digitar números < 0 e números > 100
if comida > 0 and comida < 100:
    b.comer(comida)
    #print("Fome: {} ".format(b.getFome()))
else:
    print("Digite um valor válido! ")
    comida = int(input("Tamagushi, Quer comer quanto? Digite entre 0 - 100!\n"))
    b.comer(comida)

remedio = int(input("Quer tomar quanto de remédio? Digite entre 0 - 100!\n"))

#Condicional para não digitar números < 0 e números > 100
if remedio > 0 and remedio < 100:
    b.tomarRemedio(remedio)
    #print("Saúde: {}".format(b.getSaude()))
else:
    print("Digite um valor válido! ")
    remedio = int(input("Quer tomar quanto de remédio? Digite entre 0 - 100!\n"))
    b.tomarRemedio(remedio)

#Condicional para saber o humor
if b.getHumor() >= 80:
    print("#Feliz")

elif (b.getHumor() >= 60 and b.getHumor() < 80):
    print("#Normal")

elif (b.getHumor() >= 30 and b.getHumor() < 60):
    print("#Triste")

else:
    print("#Terminal")


