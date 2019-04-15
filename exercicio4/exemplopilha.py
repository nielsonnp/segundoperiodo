''' Armazene os livros que você pegou na biblioteca do IFPB criando pilhas de
acordo com as disciplinas.'''

class PilhaDeLivros:
    def __init__(self):
        self.pilha = []

    def empilhar(self, livro):
        self.pilha.append(livro)

    def desempilhar(self):
        if self.vazio() == False:
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


class Biblioteca:
    def __init__(self):
        self.biblioteca = {}

    def add_pilha(self, disciplina):
        self.biblioteca[disciplina] = PilhaDeLivros()

    def empilhar_livro(self, disciplina, livro):
        if (disciplina in self.biblioteca.keys()):
            pilha = self.biblioteca[disciplina]
            pilha.empilhar(livro)

    def dempilhar_livro(self, disciplina):
        if (disciplina in self.biblioteca.keys()):
            pilha = self.biblioteca[disciplina]
            pilha.desempilhar()

    def livro_do_topo(self, disciplina):
        if (disciplina in self.biblioteca.keys()):
            pilha = self.biblioteca[disciplina]
            return pilha.topo()
        return None

    def nenhum_livro(self, disciplina):
        pilha = self.biblioteca[disciplina]
        return pilha.vazio()


b1 = Biblioteca()

b1.add_pilha('Português')
b1.add_pilha('Matemática')

b1.empilhar_livro("Português", "Port. Bás 1")
b1.empilhar_livro("Português", "Port. Bás 2")
b1.empilhar_livro("Português", "Port. Bás 3")

print(b1.livro_do_topo("Português")) #Port. Bás 3

b1.empilhar_livro("Matemática", "Mat. Bás 1")
b1.empilhar_livro("Matemática", "Mat. Bás 2")
b1.empilhar_livro("Matemática", "Mat. Bás 3")

print(b1.livro_do_topo("Matemática")) #Mat. Bás 3

b1.dempilhar_livro("Matemática")
print(b1.livro_do_topo("Matemática")) #Mat. Bás 2

