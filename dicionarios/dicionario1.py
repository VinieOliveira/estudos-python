d1 = {'chave1': 'valor da chave 1', 'chave1': 'valor da chave 1 final'} #se duplicar, o ultimo que conta como valor final.
d2 = dict(chave2='Valor da chave 2', chave3= 'valor da chave 3')

d1['nova chave'] = 'valor da chave nova'

print(d1['chave1'])
print(d2)

d4 = {1: "vinicius", 2: "Jamily"}

print(f'{d4[1]} e {d4[2]}')
