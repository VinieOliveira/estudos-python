#CRIE UMA FUNÇÃO QUE RECEBE UMA FUNÇÃO 2 COMO PARAMETRO E RETORNE O VALOR DA FUNCAO 2 EXECUTADA.


def ola_mundo():
    return 5+5
    

def mestre(funcao):
    return funcao()


executando = mestre(ola_mundo)
print(executando)