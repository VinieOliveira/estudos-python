lista1 = ['comer', 'cagar', 'defecar']
print(lista1)

def remover_item(lista):
    lista.pop()
    return lista

resultado_funcao = remover_item(lista1)

print(resultado_funcao)

print(lista1)