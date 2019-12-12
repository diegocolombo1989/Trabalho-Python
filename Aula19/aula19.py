# Para abrir um arquivo para leitura

arquivo = open('cadastro.txt', 'r')
# Conteúdo






# lista_do_arquivo = conteudo.split('\n')

# primeiro linha = lista_do_arquivo[0]






# for linha in arquivo:
#     # print(linha)
#     campos = linha.split(',')

#     # print(f'{campos[1]: {campos[3]}')

#     for campo in campos:
#         print(linha)
#         linha.s

registros = []
campos = ('codigo', 'nome', 'sexo', 'idade')
for linha in arquivo:
    campos = linha.strip().split(',')
    dicio = {}
    dicio['codigo'] = campos[0]
    dicio['nome'] = campos[1]
    dicio['sexo'] = dados[2]
    dicio['idade'] = dados[3]

for campo in campos:
    dicio[campo] = dados[contador]
    contador = contador + 1