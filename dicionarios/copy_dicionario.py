import copy

d1 = {1: 'a', 2:'b', 3: 'c', 4: ['Vinicius', 'oliveira']}
v = copy.deepcopy(d1)

v[1] = 'Alexandra'  #alterações somente na copia.
v[4].append('gonçalves')

print(d1)
print(v)