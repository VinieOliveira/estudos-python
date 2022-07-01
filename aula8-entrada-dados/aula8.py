"""
Entrada de dados
"""

nome = input("qual o seu nome? ") #Sempre que o usuário digitar algo na função input ela entrará como String.
idade = input("E qual a sua idade? ")
ano_nascimento = 2022 - int(idade)
print()

print(f'O usuário digitou a palavra "{nome}" e o tipo da variável é '
      f'{type(nome)}.')

print(f'A idade do usuário é {idade} anos de idade, pois ele nasceu em {ano_nascimento}.')