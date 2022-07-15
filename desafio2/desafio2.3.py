nome = input("Digite seu primeiro nome: ")

len_nome = len(nome)


if len_nome <= 4:
    print("seu nome é curto!")

elif len_nome > 4 and len_nome <= 6:
    print("seu nome é normal")

else:
    print("seu nome é grande!!!")