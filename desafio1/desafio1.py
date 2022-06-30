nome = 'vinicius'; idade = 28; altura = 1.70; peso = 63; ano = 2022
nasc = ano - idade
imc = peso / (altura ** 2)

print('Olá {}, tudo bem? Sua idade é {} anos de idade; '
      'sua altura é {:.2f} de altura e seu peso é {}kg.'.format(nome, idade, altura, peso))

print('Você nasceu no ano de {} e tem o IMC {:.2f}.'.format(nasc, imc))