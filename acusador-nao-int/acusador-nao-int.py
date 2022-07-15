num1 = input("Digite um número: ")
num2 = input(("Digite outro número: "))

"""if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1+num2)

else:
    print("não consigo somar porque você não digitou dois numeros inteiros.")"""

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('Error')


    #PAREI NO MEIO DA AULA COM SONO
