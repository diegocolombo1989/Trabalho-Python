# 1 - Criar um programa para o cadastro do cliente
# 2 - Para cadastro de Clientes deve pedir os seguintes dados:
# 3 - Codigo do Cliente, CPF, NomeCompleto:
# 4 -data de nascimento, estado, cidade, cep, bairro, rua, numero da casa, complemento.


def cadatro_cliente(numero_funcao):
    dados_cliente = ['Codigo do Cliente', 'CPF', 'Nome Completo', 'data de nascimento', 'estado', 'cidade', 'cep',
                    'bairro', 'rua', 'numero casa', 'complemento']

    lista = []

    for j in range(numero):
        dicionario = {}

        for i in dados_cliente:
            dicionario[i] = input(f'{i}: ')
        lista.append(dicionario)
    return lista

numero = int(input('Digite o numero de cadastros: '))

lista_cadastro = cadastro_cliente(numero)

# Criar uma função para salvar em arquivo:

for cliente in lista_cadastro:
        cliente chave = list)cliente.keys())
    for chaves in cliente chave:
        salva = (f'{cliente[chaves]}')
        