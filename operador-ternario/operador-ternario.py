logado = True

msg = 'usuário logado ' if logado else "Usuário desconectado"
print(msg)

idade = input("Qual sua idade? ")
if not idade.isnumeric():
    print('Você precisa digitar um numero abestado')
else:
    idade = int(idade)
    maior = idade >= 18
    msg = 'pode acessar' if maior else "não pode"

    print(msg)