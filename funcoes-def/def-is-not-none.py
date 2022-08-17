def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print("idade não existe")

lista = [1,2,3,4,5,6]
lista2 = [10,20,30,40,50]

func(*lista, *lista2, nome='vinicius', sobrenome= 'oliveira', idade=28)