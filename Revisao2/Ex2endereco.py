
# Crie uma classe endereco 3 atributos 7 metodos

class Endereco:
    def __init__(self, logradouro:str, numero:int, cep:int):
        self.__logradouro = ''
        self.__numero = 0
        self.__cep = 0

        if type(logradouro) == str:
            self.__logradouro = logradouro
        if type(numero) == int:
            self.__numero = numero 
        if type(cep) == int:    
            self.__cep = cep

    def __verifica_dados(self, logradouro, numero, cep) -> bool:
        if type(logradouro) == str and numero == int  and cep == int:
            return True
        return False
        
    def set_logradouro(self, logradouro):
        self.logradouro = logradouro

    def set_numero(self, numero):
        self.numero = numero

    def set_cep(self, cep):
        self.cep = cep

    def get_logradouro(self):
        return self.get_logradouro

    def get_numero(self):
        return self.get_numero

    def get_cep(self):
        return self. get_cep


