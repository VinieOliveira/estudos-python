nome = input("Qual o seu nome? ")

print(nome or "você não digitou nada")

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'vini'

print(a or b or c or d or e or f or g) '''Vai retornar 22 pq é a primeira verdadeira'''