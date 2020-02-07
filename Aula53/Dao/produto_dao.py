import MySQLdb

from Aula53.Model.produto_model import ProdutoModel

class ProdutoDao:
    def __init__(self):
        self.connection = MySQLdbconnect(host='local', database= 'aulabd', user='root', passwd='')
        self.cursor = self.connection.cursor()

        def listar_todos(self):
            self.cursor = cursor.execute("SELECT * FROM produto")
            produto = self.cursor.fetchall()
            lista_produto = []

            for p in produto:
                produto = ProdutoModel(p[1], p[2], p[0])
                lista_produto.append(produto.__dict__)
            return lista_produto