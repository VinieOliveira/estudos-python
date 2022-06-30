nome = 'Vinícius'  #o = é um sinal de atribuição.
idade = 32
altura = 1.70
e_maior = idade > 18
data_atual = 2022
peso = 63
imc = peso / (altura ** 2)

print('Seu nome é', nome + ', você tem', idade, 'anos de idade e pesa', peso, 'kg. Seu IMC é', imc)

#AGORA UM JEITO MAIS FÁCIL DE IMPRIMIR A LINHA 9

print(f'Seu nome é {nome}, você tem {idade} anos de idade e pesa {peso}kg. Seu IMC é {imc:.2f}.') #preste atenção na formatação do float.


print('Seu nome é {0} {0}, você tem {1} anos de idade e pesa {2}kg. Seu IMC é {3:.2f}.'.format(nome, idade, peso, imc))
