clientes = {
    'Cliente1' : {
        'nome': 'Vinicius',
        'sobrenome': 'Oliveira',
    },
    'Cliente2' : {
        'nome': 'Jamily',
        'sobrenome': 'Ribeiro',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
