from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
        return

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 199999)
        return rand





p1 = Pessoa.por_ano_nascimento("vinicius", 1994)
p2 = Pessoa("vinicius", 28)
print(p1)
print(p2)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
p2.get_ano_nascimento()

print(Pessoa.gera_id())
print(p2.gera_id())
print(p2.gera_id())
print(p1.gera_id())