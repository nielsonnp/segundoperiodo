'''3. Faça um programa que contenha a classe que represente uma Conta Corrente. A classe
deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios.'''


class ContaCorrente:

    def __init__(self, numero, nomeCorrentista, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

numero1 = input("Digite o número da conta: ")
nome = input("Digite o nome do cliente: ")
print("=============================")
conta = ContaCorrente(numero1, nome)

print('Número da conta: {} '.format(conta.numero))
print('Nome do Cliente: {} '.format(conta.nomeCorrentista))

print("===== Escolha uma Opção: ====")
acao = int(input("1 Deposito - 2 Saque: \n"))#Coloca o cursor no final

if acao == 1:
    print("Quer depositar quanto? ")
    digiteValor = int(input(" "))
    conta.deposito(digiteValor)
    print("Saldo: {}".format(conta.saldo))
elif acao == 2:
    print("Quer sacar quanto? ")
    digiteValor = int(input(" "))
    if digiteValor > conta.saldo:
        print("Saldo insuficiente! ")
    else:
        conta.saque(digiteValor)
        print("Saldo: {}".format(conta.saldo))
else:
    print("Número inválido!")



