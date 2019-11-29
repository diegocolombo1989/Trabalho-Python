# AUla 11 - 21-11-2019
# Prova

#--- 1- Crie um programa que calcule o imposto ISS de um serviço de desenvolvimento de software, utilizar métodos

#--- 2- Crie um programa que calcule a rentabilidade anual de um investimento baseando-se em sua rentabilidade mensal (juros compostos), 
# a rentabilidade deve ser apresentada em % e R$, utilizar métodos

#--- 3-
#--- 4-
#--- 5-


from calc_exerc1 import calculo_imposto

print('='*50)
print('\n'*3)

nome = input('QUal o serviço:\n')
print('Qual o valor do software:')
preco = float(input('R$ '))



imposto = calculo_imposto(preco)

print(f'O total de imposto é: {imposto}')


print('='*50)