string = 'O brasil é penta'
lista = string.split(' ')
print(lista)

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])