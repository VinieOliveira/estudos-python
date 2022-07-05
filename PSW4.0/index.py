nota1 = input("Digite sua primeira nota: ") #aqui também poderia colocar o input dentro do int para converter
nota2 = input("Digite sua segunda nota: ")
print("Vamos ver sua média...")
media = (float(nota1) + float(nota2)) /2

if media >= 8:
    print ("Parabéns, você passou! Sua média é {}!".format(media))
elif media >= 6:
    print(f"recuperação, sua média é {media}")
else:
    print ("Parabéns, você não passou! HAHA, sua média é {}".format(media))

    #A AULA PAROU EM 31M
    