

nome = input('Digite o nome da cerveja: ')
marca = input('Digite a marca da cerveja: ')
tipo = input('Digite a idade: ')
teor = float(input('Digite o teor alcoólico: '))
cerveja = {'Nome': nome, 'Marca': marca, 'Tipo': tipo, 'Teor': teor}


def cervejao(cerveja_dicionario):
    arquivo = open('aula15.txt','r')
    arquivo.write(f"{cerveja_dicionario['nome']};{cerveja_dicionario['marca']};{cerveja_dicionario['tipo']};{cerveja_dicionario['teor']}")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt','r',)
        for lista in arquivo:
        cerveja = {'nome': lista_linha[0], 'marca':lista_linha{1}, 'tipo':lista_linha[2], 'teor':lista_linha[3]}
        lista.append(cerveja)
    arquivo.close()
    return lista

for c in ler():
    print(f"{c['nome']} - {c['marca']} - {c['tipo']} - {c['teor']}")