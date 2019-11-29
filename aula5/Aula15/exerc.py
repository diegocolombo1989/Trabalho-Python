############################################ área do metodo ################################################

def cervejao(cerveja_dicionario):
    arquivo = open('aula15.txt','a')
    arquivo.write(f"{cerveja_dicionario['nome']};{cerveja_dicionario['marca']};{cerveja_dicionario['tipo']};{cerveja_dicionario['teor']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt','r',)
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'nome': lista_linha[0], 'marca':lista_linha[1], 'tipo':lista_linha[2], 'teor':lista_linha[3]}
        lista.append(cerveja)
    arquivo.close()
    return lista

########################################## area do código #################################################

nome = input('Digite o nome da cerveja: ')
marca = input('Digite a marca da cerveja: ')
tipo = input('Digite o tipo: ')
teor = float(input('Digite o teor alcoólico: '))
cerveja = {'nome': nome, 'marca': marca, 'tipo': tipo, 'teor': teor}

cervejao(cerveja)


for c in ler():
    print(f"{c['nome']} - {c['marca']} - {c['tipo']} - {c['teor']}")