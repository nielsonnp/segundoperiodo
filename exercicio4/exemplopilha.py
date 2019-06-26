class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, livro):
        self.pilha.append(livro)

    def desempilhar(self):
        if (self.vazio() == False):
            self.pilha.pop(len(self.pilha) -1)

    def topo(self):
        if (self.vazio() == False):
            return self.pilha[len(self.pilha) -1]
        return None

    def vazio(self):
        if (len(self.pilha) == 0):
            return True
        else:
            return False

    def tamanho(self):
        return len(self.pilha)


class GuardaRoupa:
    def __init__(self):
        self.guarda_roupa = Pilha()
        self.cama = Pilha()

    def guardar_roupa(self, peca):
        self.guarda_roupa.empilhar(peca)

    def tirar_peca(self, peca):
        while True:
            roupa = self.guarda_roupa.topo()
            print(roupa)
            if (roupa != peca):
                self.guarda_roupa.desempilhar()
                self.cama.empilhar(roupa)

            else:
                self.guarda_roupa.desempilhar()
                for i in range(self.cama.tamanho()):
                    topo = self.cama.topo()
                    self.cama.desempilhar()
                    self.guarda_roupa.empilhar(topo)

                break


r = input("Qual roupa? ")

g = GuardaRoupa()

while (r != '-1'):
  g.guardar_roupa(r)
  r = input("Qual roupa? ")

print("Saiu!")

roupa_desejada = input("Você quer qual roupa? ")
g.tirar_peca(roupa_desejada)





