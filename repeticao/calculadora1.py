while True:
    num_1 = input("Digite um numero: ")
    num_2 = input("Digite o segundo numero: ")
    op = input("digite um operador: ")


    if not num_1.isnumeric() or not num_2.isnumeric():
        print("você precisa digitar somente números")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if op == '+':
        resultado = num_1 + num_2
        print(f"{num_1} {op} {num_2} = {resultado}")
        sair = input("Deseja sair? ([s]im ou [n]ão) ")
        if sair == 's':
            print("obrigado!")
            break

    elif op == '-':
        resultado = num_1 - num_2
        print(f"{num_1} {op} {num_2} = {resultado}")
        sair = input("Deseja sair? ([s]im ou [n]ão) ")
        if sair == 's':
            print("obrigado!")
            break

    elif op == '*':
        resultado = num_1 * num_2
        print(f"{num_1} {op} {num_2} = {resultado}")
        sair = input("Deseja sair? ([s]im ou [n]ão) ")
        if sair == 's':
            print("obrigado!")
            break

    elif op == '/':
        resultado = num_1 / num_2
        print(f"{num_1} {op} {num_2} = {resultado}")
        sair = input("Deseja sair? ([s]im ou [n]ão) ")
        if sair == 's':
            print("obrigado!")
            break

