lista = ['vini', 'maria', 'outra lista', 'foi criada automaticamente', 'por conta do asterisco']

n1, n2, *outra_lista = lista #aqui pode ser feito pra adicionar uma lista nos ultimos valores ou no começo

print(n1, n2, outra_lista)

*outra_lista, n1, n2 = lista #VEJA AQUI O QUE FALEI ACIMA
print(n2)