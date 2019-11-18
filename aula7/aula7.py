# Aula 7 - 14-11-2019
# Dicionarios

lista = []

dicionario = { 'Nome':'Diego', 'Sobrenome':'Colombo' }
print(dicionario)
print(dicionario ['Sobrenome'])

Nome = 'Diego'
lista_notas = [10,20,50,70]
media = sum(lista_notas)/ len(lista_notas)
situacao = 'Reprovado'
if media >=7:
    situacao = 'Aprovado'
    dicionario_alunos = { 'Nome':Nome, 'Lista_notas':lista_notas, 'Media': media, 'Situacao':situacao }

    print(f"{dicionario_alunos[ 'Nome' ]} - {dicionario_alunos[ 'Situacao' ]} ")