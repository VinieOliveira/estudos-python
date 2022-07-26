variavel = ['vinicius', 'Jairla', 'oaquim']

comeca_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_j = True

if comeca_j:
    print("Existe uma palavra que começa com jota")
else:
    print("não existe palavra que começa com j")