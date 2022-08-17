"""
fizz Buzz - Se o parametro  da função for divisível por 3, retorne fizz, se o parÂmetro da função for divi
sível por 5, retorne buzz. Se for por 3 e 5 retorne 'Fizzbuzz" senão, retorne pelo numero enviado
"""
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzBUZZ, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz,  {n} é divisível por 3'

    return n

from random import randint

for i in range(100):
    aleatório = randint(0, 100)
    print(fb(aleatório))
