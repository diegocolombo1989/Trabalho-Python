from flask import Flask
from flask_restful import Api

from Aula41.Controllers.endereco_controller import EnderecoController

app = Flask(__name__)
api = Api(app)

api.add_resource(EnderecoController, '/api/endereco', endpoint='enderecos')
api.add_resource(EnderecoController, '/api/endereco/<int:id>', endpoint='endereco')

@app.route('/')
def index():
    return 'Teste API do Endereco'


app.run(debug=True)