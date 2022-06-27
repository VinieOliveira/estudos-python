"""
Tipos de dados

str- string
int- inteito - 123456 0 -10 
float- real/ponto flutuante - 0.9 (tem ponto, nunca vígula)
bool- booleano/lógico - True ou False  ex: "10==10 - True"
"""
#python é uma linguagem interpretada de tipagem dinaima, se ele ler um código ele ja sabe de que tipo é.

print('Vinicius', type('vinicius')) #essa função type retorna o tipo do valor
print(10, type(10))
print(1.0,type(1.0))
print("l"=="L",type("l"=="l"))

#PARA CONVERTER UM NUMERO

print(int('10')) #converter assim pra inteiro da certo
print(float('2.5')) #assim pra float também da certo
#print(int("vinicius")) agora assim dá errado mané.

#EXERCÍCIO

print('vinicius', type('vinicus'))
print('18', type('int'))
print('1.70', type('1.70'))
print(28 > 18, type(28>18))