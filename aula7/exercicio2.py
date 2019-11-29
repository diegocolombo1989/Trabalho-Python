# Exercicio 2 - Dicionarios
#Escreva um programa que leia os dados de 11 jogadores
# Jogador: nome, posicao, numero, pernaboa
#Crie um dicionario para armazenar os dados
# Imprima todos os jogadores e seus dados

dicionario_jogadores = { 'Nome':'', 'Posicao':'', 'numero':'', 'pernaboa':'' }
lista = []
for i in range(1,3):
    dicionario_jogadores ['Nome'] = input('Digite seu Nome: ')
    dicionario_jogadores ['Posicao'] = input('Qual sua posição: ')
    dicionario_jogadores ['numero'] = int(input('Qual seu numero: '))
    dicionario_jogadores ['pernaboa'] = input('Qual sua perna boa: ')

lista.append(dicionario_jogadores)
print(f"{dicionario_jogadores['Nome']} - Posicao: {dicionario_jogadores['Posicao']} - numero: {dicionario_jogadores['numero']} - Perna Boa: {dicionario_jogadores['pernaboa']}"}