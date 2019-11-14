# 2
#  Mercado tech ----
# Solicitar nome do funcionario
# solicitar idade
# informar se o funcionario pode adquirir produtos alcoolicos

#3
# Cadastro produtos mercado tech
# solicitar o nome do produto
# Solicitar a categoria do produto (alcoolicos e não alcoolicos)
# Exibir o produto cadastrado
print('Mercado Tech')
print('-'*50)

nome = (input('Nome do funcionario: '))
idade = int(input('Idade: '))


if idade > 18:
    print('Funcionário pode beber' )
else:
    print('funcionário não pode beber')


