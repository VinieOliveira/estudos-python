contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = contador + acumulador
    contador += 1

else:
    print("cheguei no else")

print("print fora do else")
