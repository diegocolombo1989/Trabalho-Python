# Crie uma classe pessoa contem 3 atributos e 7 metodos

class Pessoa:
    def __init__(self, nome:str, sobrenome:str, idade:int) -> None:
        self.__nome = input('seu nome: ')
        self.__sobrenome = input('seu sobrenome: ')
        self.__idade = 0

        if type(nome) == str:
            self.__nome = nome
        if type(sobrenome) == str:
            self.__sobrenome = sobrenome
        if self.__verifica_idade(idade):
            self.__idade = idade

    def __verifica_idade(self, idade) -> bool:
        if type(idade) == int and idade > 0:
            return True
        return False

    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def set_idade(self,idade):
        self.idade = idade

    def get_nome(self, __nome):
        return self.get_nome

    def get_sobrenome(self):
        return self.get_sobrenome

    def get_idade(self):
        return self.get_idade

p = Pessoa('', '', 0)

print(p.get_nome())
