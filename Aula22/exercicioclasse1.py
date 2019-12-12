

# Aula 21 09 12 -2019

# Crie uma classe cliente:

# 1 - Deve ter como atributos: codigo, cpf, idade, sexo

# 2 - Como métodos: receber salario, comprar pagar divida

#  QUando recebe aumenta o dinheiro na carteira.

#  Quando compra aumenta os bens e diminui o dinheiro na carteira

#  Se comprar e não tiver dinheiro suficiente deve diminuir o dinheiro da carteira e aumentar a divida.

#  Para pagar a divida tem que ter dinheiro suficiente na carteira

# 3 - Atributs de estado: dinheiro na carteira, divida, bens

class Cliente:

    def __init__(self, nome1, codigo1, cpf1, idade1, sexo1):
        self.nome = nome1
        self.codigo = codigo1 
        self.cpf = cpf1        
        self.idade = idade1
        self.sexo = sexo1

        self.divida = 0
        self.dincarteira = 0
        self.bens = 0
        self.comprar = 0

    def receber (self,salario):
        if self.dincarteira == 0:
            self.dincarteira = salario
        else:
            self.dincarteira = self.dincarteira + salario
    
    def comprar (self,compras):
        if self.comprar > 0:
            self.bens = self.bens + self.comprar
            self.dincarteira = self.dincarteira - self.comprar
        elif self.comprar < self.dincarteira:
            self.dincarteira -= self.dincarteira
            self.divida += self.divida
        elif self.dincarteira >= self.divida:
            self.divida == self.divida - self.dincarteira


c = Cliente('Diego', 4, 443434329, 30, 'm')

c.receber(100)

print(f'nome: {c.nome1}')
print(f'Código: {c.codigo1}') 
print(f'CPF: {c.cpf1}')
print(f'Idade: {c.idade1}')
print(f'Sexo: {c.sexo1}')





        



