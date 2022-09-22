from pessoa import Pessoa

p1 = Pessoa("Vinicius", 28)

p1.falar('Bosta')
p1.comer("cravo")

p2 = Pessoa("Gorete", 60)

p2.falar("vida")
p2.parar_de_falar()

print(p1.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
