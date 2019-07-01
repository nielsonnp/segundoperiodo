
#Começo classe Nó
class No:

    def __init__(self, dado, dir, esq):
        self.pai = None
        self.dado = dado
        self.dir = dir
        self.esq = esq

    # Getters e setters
    def getPai(self):
        return self.pai

    def setPai(self, pai):
        self.pai = pai

    def getDado(self):
        return self.dado

    def setDado(self, dad):
        self.dad = dad

    def getDir(self):
        return self.dir

    def setDir(self, dir):
        self.dir = dir

    def getEsq(self):
        return self.esq

    def setEsq(self, esq):
        self.esquerdo = esq

#começo classe árvore
class Arvore:

    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    def inserir(self, v):
        novo = No(v, None, None)  # cria um novo Nó
        if self.root == None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.dado:  # ir para esquerda
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return

                else:  # ir para direita
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return

    def buscar(self, chave):
        if self.root == None:
            return None  # se arvore vazia
        atual = self.root
        while atual.dado != chave:
            if chave < atual.dado:
                atual = atual.esq
            else:
                atual = atual.dir
            if atual == None:
                return None
        return atual

    def nosucessor(self, apaga):
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.dir

        while atual != None:
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq


        if sucessor != apaga.dir:
            paidosucessor.esq = sucessor.dir
            sucessor.dir = apaga.dir
        return sucessor

    def remover(self, v):
        if self.root == None:
            return False  # se arvore vazia
        atual = self.root
        pai = self.root
        filho_esq = True

        while atual.dado != v:
            pai = atual
            if v < atual.dado:
                atual = atual.esq
                filho_esq = True
            else:
                atual = atual.dir
                filho_esq = False
            if atual == None:
                return False


        if atual.esq == None and atual.dir == None:
            if atual == self.root:
                self.root = None
            else:
                if filho_esq:
                    pai.esq = None
                else:
                    pai.dir = None


        elif atual.dir == None:
            if atual == self.root:
                self.root = atual.esq
            else:
                if filho_esq:
                    pai.esq = atual.esq
                else:
                    pai.dir = atual.esq


        elif atual.esq == None:
            if atual == self.root:
                self.root = atual.dir
            else:
                if filho_esq:
                    pai.esq = atual.dir
                else:
                    pai.dir = atual.dir


        else:
            sucessor = self.nosucessor(atual)

            if atual == self.root:
                self.root = sucessor
            else:
                if filho_esq:
                    pai.esq = sucessor
                else:
                    pai.dir = sucessor
            sucessor.esq = atual.esq

        return True

    def ordem(self, atual):
        if atual != None:
            self.ordem(atual.esq)
            print(atual.dado, end=" ")
            self.ordem(atual.dir)

    def pre_ordem(self, atual):
        if atual != None:
            print(atual.dado, end=" ")
            self.pre_ordem(atual.esq)
            self.pre_ordem(atual.dir)

    def pos_ordem(self, atual):
        if atual != None:
            self.pos_ordem(atual.esq)
            self.pos_ordem(atual.dir)
            print(atual.dado, end=" ")


    def minimo(self):
        atual = self.root
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.esq
        return anterior

    def maximo(self):
        atual = self.root
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.dir
        return anterior

    def imprimir(self):
        print(" Resultado: ")
        print(" Pré-ordem: ", end="")
        self.pre_ordem(self.root)
        print("\n Ordem: ", end="")
        self.ordem(self.root)
        print("\n Pos-ordem: ", end="")
        self.pos_ordem(self.root)
        if self.root != None:
            print("\n Mínimo: {}" .format(self.minimo().dado))
            print(" Máximo: {}" .format(self.maximo().dado))

#fim da classe

a = Arvore()
print("Arvore Binaria")
opcao = 0
while opcao != 5:
    print("Entre com a opcao: ")
    print("1 - Inserir")
    print("2 - Excluir")
    print("3 - Pesquisar")
    print("4 - Exibir")
    print("5 - Sair do programa")

    opcao = int(input("-> "))
    if opcao == 1:
        x = int(input(" Digite um número: "))
        a.inserir(x)
    elif opcao == 2:
        x = int(input(" Digite um número: "))
        if a.remover(x) == False:
            print(" Número não encontrado!")
    elif opcao == 3:
        x = int(input(" Digite um número: "))
        if a.buscar(x) != None:
            print(" Número Encontrado")
        else:
            print(" Número não encontrado!")
    elif opcao == 4:
        a.imprimir()
    elif opcao == 5:
        break