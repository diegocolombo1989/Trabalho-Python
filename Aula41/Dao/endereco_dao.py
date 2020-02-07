import MySQLdb

from Aula41.Model.endereco_model import EnderecoModel

class EnderecoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM endereco")
        endereco = self.cursor.fetchall()
        lista_endereco = []
        for e in endereco:
            endereco = EnderecoModel(e[1], e[2], e[3], e[4], e[5], e[0])
            lista_endereco.append(endereco.__dict__)
        return lista_endereco

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM endereco WHERE ID = {}".format(id))
        endereco = self.cursor.fetchone()
        e = EnderecoModel(endereco[1], endereco[2], endereco[3], endereco[4], endereco[5], endereco[0])
        return e.__dict__

    def insert(self, endereco : EnderecoModel):
        self.cursor.execute("""
            INSERT INTO endereco 
            (LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE) 
            VALUES('{}',{},'{}','{}','{}')""".format(endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade))
        self.connection.commit()
        id = self.cursor.lastrowid
        endereco.id = id
        return endereco.__dict__

    def update(self, endereco : EnderecoModel):
        self.cursor.execute("""
            UPDATE endereco 
                SET 
                    LOGRADOURO = '{}',
                    NUMERO = {},
                    COMPLEMENTO = '{}',
                    BAIRRO = '{}',
                    CIDADE = '{}'
                WHERE ID = {}
        """.format(endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.id))
        self.connection.commit()
        return endereco.__dict__

    def remove(self, id):
        self.cursor.execute(f"DELETE FROM endereco WHERE ID = {id}")
        self.connection.commit()
        return f'Removido o endereco de id : {id}'
