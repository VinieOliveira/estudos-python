def func(arg, arg2):
    return arg * arg2

var  = func(2,2)

print(var)

#veja agora a diferença de uma função normal pra aninima

a = lambda x, y: x * y #fução anonima pq nao tem nome, estou jogando isso dentro de uma variável

print(a(2, 3))
