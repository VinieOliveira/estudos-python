t1 = 1,2,'vulto',4,5
t2 = 6,7,8,9,10
t3 = t1+t2

n1, n2, n3, *_, n9, n10 = t3
print(n9)
print(t2)
print('---- for começa  abaixo---')

for i in t3:
    print(i)

#se quiser alterar tupla tem que converter primeiro em lista

t1 = list(t1)
t1[3] = "Fantasma"
print('---abaixo com alteração da tupla convertida em lista depois em tupla novamente-------')
t1 = tuple(t1)
print(t1)

