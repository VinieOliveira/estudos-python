secreto = "perfume"
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("ah!!! Isso não vale! Digite apenas uma letra! ")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Que legal!!! a letra {letra} existe na palavra segreta')
    else:
        print(f'Aff! a letra {letra} não existe na palavra secreta')
        digitadas.pop()

    print(digitadas)
'''parou em 40m de aula'''