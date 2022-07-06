from unittest import result


def exibe_bom_dia():          #crio a função
    print("Bom dia! Tudo bem?")

exibe_bom_dia()                #chamo a função

def soma(n1, n2):             #crio uma função que recebe parametros
    resultado = n1 + n2
    return(resultado)

def multiplica(n1, n2):
    resultado = n1 * n2
    return(resultado)

soma_total = soma(2, 3)       #chamo a função e dou os parametros
multiplicacao = multiplica(5, 5)
print(soma_total)
print(multiplicacao)

