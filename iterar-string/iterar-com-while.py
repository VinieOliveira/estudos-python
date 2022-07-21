frase = 'Como uma deusa' #tudo que tem índice é iterável
tamanho = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input("qual letra você quer deixar maiúsculo ? ")

while contador < tamanho:  #iteração
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra

    contador += 1
print(nova_string)