''' Ordene as pessoas que precisam ser atendidas em um banco, informando
quem é o primeiro e o último a ser atendido.'''

class Fila:
    def __init__(self):
        self.fila = []

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

class FilaUnica:
    def __init__(self):
        self.fila_unica = Fila()

    def entrar_na_fila(self, pessoa):
        self.fila_unica.entrar(pessoa)

    def sair_da_fila(self):
        self.fila_unica.sair()

    def proximo_da_fila(self):
        proximo = self.fila_unica.primeiro()
        self.fila_unica.sair()
        return proximo

    def ultimo_da_fila(self):
        return self.fila_unica.ultimo()


banco = FilaUnica()

while True:

    b1 = input("Nome: ")

    if b1 == '-1':
        break
    else:
        banco.entrar_na_fila(b1)


print('Primeiro da fila: {}'.format(banco.proximo_da_fila()))

print('Último da fila: {}' .format(banco.ultimo_da_fila()))

'''banco.entrar_na_fila('Ramon')
banco.entrar_na_fila('Ranyelson')
banco.entrar_na_fila('Alan')


print(banco.proximo_da_fila())
print(banco.proximo_da_fila())
print(banco.proximo_da_fila())

print(banco.ultimo_da_fila())'''