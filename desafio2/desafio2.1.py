#programa criado pra verificar se o número é inteiro, e par ou impaar, se não for inteiro, acusa.
num = input("Digite um número inteiro: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f"O numero {num} é par! ")
    else:
        print(f"O numero {num} é impar!")

else:
    print(f"'{num}' não é um numero inteiro! Tente novamente!")
