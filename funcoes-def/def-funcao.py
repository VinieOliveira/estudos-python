def funcao(msg="Olá", nome="senhor(a)"):
    nome = nome.replace('e', '3')
    msg = msg.replace("i", '!')
    print(msg, nome)

funcao("olá", "gabriel")
funcao("bom dia", "gigliola")
funcao("viva", "seu gustavo")
funcao() #se nao preencher nada printa padrão
funcao(nome="vinicius", msg="Ei") #assim permite especificar o que é cada coisa independente da ordem
funcao("venicius", "ei") #sem especificar, vai na ordem padrão, logo pode dar errado em alguns casos
