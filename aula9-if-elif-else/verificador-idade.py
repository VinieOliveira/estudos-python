nome = input("Digite seu nome: ")
idade = int(input("digite sua idade: "))

idade_minima = 18
idade_máxima = 60


if idade >= idade_minima and idade <= idade_máxima:
    print(f"{nome}, você pode pegar o emprestimo!")

else:
    print(f"{nome}, você não pode pegar o empréstimo!")