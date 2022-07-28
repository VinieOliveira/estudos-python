""" Split - divie string
    Join - junta string
     Enumerate -  enumera elementos iteraveis"""

string = "O Brasil não é *um país pra todos , é merda Brasil"
lista_1 = string.split(' ') #divide-se onde tem o espaço
lista_2 = string.split(',') #divide-se onde tem a lista
lista_3 = string.split('*') #divide-se onde tem o asterisco
'''print(lista_1)
print(lista_2)
print(lista_3)'''

palavra = ''
contagem = 0
impresso = 0

for valor in lista_1:
    quant_vezes = lista_1.count(valor)

    if quant_vezes > contagem:
        contagem = quant_vezes
        palavra = valor

    print(f'a palavra "{valor}" apareceu {lista_1.count(valor)}x na frase')
print(f'A palavra que apareceu mais vezes é "{palavra}", que apareceu {contagem}x')
