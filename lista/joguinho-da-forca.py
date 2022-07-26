secreto = "bosta"
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print("Você perdeu!")
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("ah!!! Isso não vale! Digite apenas uma letra! ")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Que legal!!! a letra "{letra}" existe na palavra segreta')
    else:
        print(f'Aff! A letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'



    if secreto_temporario == secreto:
        print(f"Parabéns, você ganhou o jogo!!! A palavra era mesmo '{secreto}'")
        break
    else:
        print(f'A palavra secretá está assim: "{secreto_temporario}"')

    if letra not in secreto:
        chances -= 1
        print(f'Você ainda tem {chances} chances')
 