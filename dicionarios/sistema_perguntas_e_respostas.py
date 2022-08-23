print('Texto explicativo')

respostas_certas = 0

perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'repostas': {
            'a': '1',
            'b': '4',
            'c': '5',

        },
        'resposta_certa': 'b',
    },
        'pergunta 2': {
        'pergunta': 'Quanto é 5*5?',
        'repostas': {
            'a': '15',
            'b': '55',
            'c': '25',

        },
        'resposta_certa': 'c',
    },
}
print()
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha as opções abaixo')
    for rk, rv in pv['repostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Sua resposta: ")
    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns!! Você acertou!')
        respostas_certas += 1
    else:
        print("ixxx! Você errou!!")
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua portentagem de acerto foi de {porcentagem_acerto:.0f}%')
