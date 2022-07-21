lista = [2,3,4,5,'fdafds', 0.6, True]

lista[4] = 'vini'
print(lista)

'''soma de listas'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2

print(lista1)
print(lista2)
print(lista3)

'''outra mandeira de juntar'''
lista1.extend(lista2)
print(lista1)
lista1.extend("a")
print(lista1)


lista4 = ["bosta"]
lista4.append("a")
print(len(lista4), lista4)

'''inserir'''
lista5 = ["lista5",1,2,3,4,5]
lista5.insert(0, "inserindo algo no valor zero")
print(lista5)

'''Deletando item da lista'''
lista5.pop(0)
print(lista5)

'''deletando um trecho'''
del(lista5[1:6])
print(lista5)
lista5.insert(3, "bosta")

'''imprimir maximo e mínimo'''
print(max(lista5), min(lista5))

'''criar lista com list e range'''
lista6 = [1, 2, 3]
print(lista6)

for valor in lista6:
    print(valor)
