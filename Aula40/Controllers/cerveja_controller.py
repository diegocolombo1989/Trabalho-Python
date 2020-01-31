<<<<<<< HEAD

from flask_restful import Resource

class CervejaController(Resource):
    def get(sejf):
=======
from flask_restful import Resource

class CervejaController(Resource):
    def get(self):
>>>>>>> f42b200bdb10b3b0609d84a3ccd6e0ef07976e2d
        return 'Acessando controladora pelo metodo HTTP GET'

    def post(self):
        return 'Acessando controladora pelo metodo HTTP POST'
<<<<<<< HEAD

    def put(self):
        return 'Acessando controladora pelo metodo HTTP PUT'

=======
    
    def put(self):
        return 'Acessando controladora pelo metodo HTTP PUT'
    
>>>>>>> f42b200bdb10b3b0609d84a3ccd6e0ef07976e2d
    def delete(self):
        return 'Acessando controladora pelo metodo HTTP DELETE'