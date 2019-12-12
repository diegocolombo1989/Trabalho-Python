

# 11 - O que uma pessoa tem? QUais as características?

##### Atributos ----- variáveis

# nome
# idade
# telefone
# sexo

# # 21 - O que uma pessoa faz?

# ##### Métodos ----- (função/procedimento)

# respira
# dorme
# corre
# bebe
# come
# multiplica

# # 3 - Como a pessoa esta agora?

# ##### Atribtos de estado ----- variaveis

# divida
# cansada
# viva
# fome
# sede

class Pessoa:
    '''
    Esta classe é uma demonstração para aula
    '''
    def __init__(self, nome1, idade1, telefone1, sexo1):

        '''
        O __init__ é o motor que irá iniciar as ariáveis da classe
        O self é o que irá conectar toda a classe
        '''
        # Atributos
          
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1

        #

        self.divida = None
        self.cansado = 'não'
        self.viva = True
        self.fome = 'não'
        self.sede = 'não'

    #### Métodos

    def respira (self, respirar):
        if respirar == True:
            self.viva = True
        else:
            self.viva = False

        

    def corre (self,distancia):
        if self.viva:
            if distancia < 100:
            self.cansado = 'pouco'
            self.sede = 'pouco'
            self.fome = 'pouco'
        elif distancia >= 100 and distancia < 200:
            self.cansado = 'medio'
            self.sede = 'medio'
            self.fome = 'medio'
        elif distancia <= 200:
            self.cansado = 'muito'
            self.sede = 'muito'
            self.fome = 'muito'
                    
        
    def dorme (self):
        if self.viva:
            self.
            self.sede = 'nao'

        
    def bebe (self):

        

    def come (self):
        pass

    def multiplica (self):
        pass




p = Pessoa('Antonio', '18', '47991955832', 'm')


p.respira = True    

p.corre(300) 
print(f'Nome é: {p.nome}')
print(f'Esta vivo? {p.viva}')
print(f'Esta com fome? {p.fome}')
print(f'Esta com sede? {p.sede}')
print(f'Esta cansado? {p.cansado}')


