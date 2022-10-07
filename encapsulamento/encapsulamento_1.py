"""public, protected, private
_ protected
__ private
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'Vinicius')
bd.inserir_clientes(2, "marilia")
bd.__dados = 'outra coisa'
print(bd.__dados)
print(bd._BaseDeDados__dados)

