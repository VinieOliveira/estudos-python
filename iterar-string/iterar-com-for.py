texto = 'python'

for letra in enumerate(texto):
    print(letra)

print('---------')
#função range recebe 3 argumentos (start= 0, stop, estep = 1) valores padrão, mas pode mudar

for n in range(0,10,1): #aqui poderia omitir 0 e 1
    print(n)
print('----------------------')

#decrementado
for n in range(20,10, -1):
    print(n)
print('-------------------')
#pra saber um multiplo de algum numero

for n in range(100):
    if n % 8 == 0:
        print(n)