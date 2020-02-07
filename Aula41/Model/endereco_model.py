class EnderecoModel:
    def __init__(self, logradouro, numero, complemento, bairro, cidade, id=0):
        self.id = id
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
