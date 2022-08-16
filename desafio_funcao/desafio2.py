#crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao 2 executada. Faça função1 executar
#duas funções que recebam um numero diferente de argumentos.

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(saudacao, 'Vini', saudacao='bom dia')
executando2 = mestre(fala_oi, "vini")
print(executando)
print(executando2)
