#Aula 17 - 02-12-2019

# 1- O rograma deve ter um menu interativao com cabeçalho, local para:
# Cadastro de clientes,
# ver cleintes cadastrados, cadastro de produtos, ver produtos cadastrados
# Venda de produtps, relatório de venda de produtos e opção sair
# Este menu deve se repetir até que a opção sair for chamada.


menu = '''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                               I FESTIVAL DE CERVEJA DE ITURORÓ                        $ 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

1 - Cadastro de Cliente
2 - Ver Clientes Cadastrados
3 - Cadastro de Produtos
4 - Ver Produtos Cadastrados
5 - Vendas
6 - Relatório de Vendas
7 - Sair

'Digite a opção desejada:') '''
opcao = (menu)
while True:
    opcao = input(menu)
    if opcao == '1':
       print('Cadastro de Cliente')
    elif opcao == '2':
       print('Ver Clientes Cadastrados')
    elif opcao == '3':
       print('Cadastro de Produtos')
    elif opcao == '4':
       print('Ver Produtos Cadastrados')
    elif opcao == '5':
       print('Vendas')
    elif opcao == '6':
       print('Relatório de Vendas')
    elif opcao == '7':
        print('Sair')
        break
    else:
        print('Valor inválido')
