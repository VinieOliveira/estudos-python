"""
Formatando valores com modificadores
:s - Texto(strings)
:d - Inteiros(int)
:f - Numeros com ponto flutuante (Float)
:.(numero) - quantidade de casas decimais(float)
:(Caractere) (> ou < ou ^)(quantidade) (tipo s, d ou f)

"""

n = 1
n2 = 1150
nome = "vinicius"
print(f'{n:0>10}') # a esquerda
print(f'{n2:0^10.5f}') # a direita
print(f'{nome:%^15}')
print(nome.ljust(15, 'c'))
print(nome.lower())
print(nome.upper())