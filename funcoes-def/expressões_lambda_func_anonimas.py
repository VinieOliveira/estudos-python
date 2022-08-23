def func(arg, arg2):
    return arg * arg2

var  = func(2,2)

print(var)

#veja agora a diferença de uma função normal pra aninima

a = lambda x, y: x * y #fução anonima pq nao tem nome, estou jogando isso dentro de uma variável

print(a(2, 3))


lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 3],
    ['p4', 8]
]
#def func (item):
    #return item[1]

lista.sort(key=lambda item: item[1], reverse=True)  #aqui ta sendo orgnaizado pela casa 1 da lista, os numeros 13, 6, etc. em ordem
print(lista)

print(sorted(lista, key= lambda i: i[0], reverse=False)) #esse i[0] é o que indica o parametro da organização da lista,
                                                     # no caso o ZERO aqui indica que vai ser organizado pelo p1, p2, em ordem.



