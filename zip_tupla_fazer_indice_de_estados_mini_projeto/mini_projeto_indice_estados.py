from itertools import zip_longest, count

indice = count()
cidades = ['são paulo', 'belo horizonte', 'Salvador', 'Monte belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    estados,
    cidades,

)

for indice, estados, cidade in cidades_estados:
    print(indice, estados, cidade)