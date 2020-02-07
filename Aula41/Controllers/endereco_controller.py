from flask_restful import Resource
from flask import request
from Aula41.Dao.endereco_dao import EnderecoDao
from Aula41.Model.endereco_model import EnderecoModel

class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()


    def post(self):
        logradouro = request.json['logradouro']
        numero = int(request.json['numero'])
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        endereco = EnderecoModel(logradouro, numero, complemento, bairro, cidade)
        msg = self.dao.insert(endereco)
        return msg

    def put(self, id):
        logradouro = request.json['logradouro']
        numero = int(request.json['numero'])
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        endereco = EnderecoModel(logradouro, numero, complemento, bairro, cidade, id)
        msg = self.dao.update(endereco)
        return msg

    def delete(self, id):
        return self.dao.remove(id)