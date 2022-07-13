nome = input("Digite um nome: ")

print(f"Você digitou '{nome}'")

ver_in = input("digite um trecho do nome para saber se faz parte deste nome: ")

if ver_in in nome:
    print(f"'{ver_in}' faz parte de '{nome}'")
else:
    print(f"'{ver_in}' não faz parte de '{nome}'")

ver_in = input(f"Agora digite um trecho para saber se NÃO FAZ PARTE de '{nome}' :")

print(f"Agora você digitou {ver_in}")

if ver_in not in nome:
    print(f"'{ver_in}' não está contido em '{nome}'")
else:
    print(f"'{ver_in}' ESTÁ SIM contido em '{nome}'")