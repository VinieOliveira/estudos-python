d1 = {
    'str': "valor",
    3:'aceita numero como chave',
    'isto_aqui_e_chave': "isto_aqui_é_valor"
}

print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())



for v in d1.values(): #tem que fazer isso pra acessar os valores
    print(v)
print('-----------')

for k in d1:
    print(k)

print('---------------')

for i in d1.items():
    print(i)

print('--------')
for k, v in d1.items():  #DESEMPACOTAR
    print(k, v)