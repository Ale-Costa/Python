
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):   
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome



class Filme(Programa):
    def __init__(self,nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} Min. - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


vingadores = Filme("Vingadores", 2012, 180)

atlanta = Serie("Atlanta", 2015, 5)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()


filme_e_serie = [vingadores,atlanta]

for programa in filme_e_serie:
    print(programa)