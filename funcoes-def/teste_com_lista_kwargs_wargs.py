def func(*args, **kwargs): #não precisa ser Args nem kwargs, isto é conveção
    print(args, kwargs)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40]
func(*lista, *lista2, nome="luis")
