class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def __str__(self):
        return ("Nome: {} - Ano: {} - Likes: {}"
                .format(self.nome, self.ano, self.likes))


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return ("Nome: {} - Ano: {} - Duração: {} - Likes: {}"
                .format(self.nome, self.ano, self.duracao, self.likes))


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return ("Nome: {} - Ano: {} - Temporadas: {} - Likes: {}"
                .format(self.nome, self.ano, self.temporadas, self.likes))


kimetsu = Filme('demon slayer - mugen train', 2021, 120)

hellsing = Serie('hellsing', 2001, 1)

filmes_e_series = [kimetsu, hellsing]

for programa in filmes_e_series:
    print(programa)
