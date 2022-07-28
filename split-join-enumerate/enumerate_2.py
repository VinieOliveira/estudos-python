lista = [
    ['gita', 'walden', 'sísifo'],
    ['filme', 'série', 'livro'],
    ['comédia','drama', 'tragédia']
]

for v1, v2 in enumerate(lista, 13):
    valor_enumerado, minha_lista = v1, v2
    nome1, nome2, nome3 = minha_lista #isto é o desempacotamento de lista
    print(nome1, nome2, nome3)
