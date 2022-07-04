"""
CONDIÇÕES IF, ELIF, ELSE
"""
num_1 = 0

if num_1 == 2:            #tudo que tiver abaixo dessa hierarquia será verdadeiro!
    print('Verdadeiro')

elif False:
    print('Agora é verdadeiro!')

elif True:
    print('Mais uma verdadera!')
else:                      #else sozinho não funciona
    print('não é verdadeiro...') #Else executa quando nenhuma das anteriores for verdadeiro.

#print('Verdadeiro 2')      #aqui ta fora do IF por conta dos espaços, OS ESPAÇOS FAZEM AS HIERARQUIAS.
