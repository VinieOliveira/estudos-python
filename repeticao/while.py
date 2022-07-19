x = 0
while x <= 10:
    y = 0
    while y < 5:
        print(f"x vale {x} e y vale {y}")
        y += 1
    if x == 3:
        x = x + 1 # se eu não colocasse isso, x não iria sair de 3 e o laço iria, portante, se repetir infinitamente..
        continue # se for um break, interrompe o laço, o CONTINUE avança pro proximo passo continuando o laço.
    print('outro ciclo')
    x = x + 1
