def funcao(var):
    print("isso será impresso por que está antes do return")
    return var #se fosse print não daria certo, testa!!!!
    print("isso nao sera impresso")

variavel = funcao("valor que eu quero")

if variavel:
    print(variavel)
else:
    print("nada")