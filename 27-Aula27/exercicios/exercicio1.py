# Aula 21 - 16-12-2019
#Funções para listas

# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?


# 1.2) Qual é o maior valor da lista2?


# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?


# 1.4) Qual é a média aritmética da lista1?


# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)


# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.


# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError


# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).


# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.


# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas

from geradorlista import lista_simples_int

from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))


# print( len(lista1))
# print( len(lista2))
# print( len(lista3))
# 1.1 print(f"O tamanho da lista 1 é: {len(lista1)}")


# 1.1 print(max(lista2))

# 1.3 print(f" A soma do maior valor com o menor valor da lista 2 é: {max(lista2) + min(lista2)}")

# 1.4 print(f" A média aritmética da lista1 é: {sum(lista1) / len(lista1)}")

# 1.5 print(f"A soma da lista 1 é: {sum(lista1)}")
# print(f"A soma da lista 1 é: {sum(lista2)}")
# print(f"A soma da lista 1 é: {sum(lista3)}")

# print(f"A soma de todas as listas é: {sum(lista1) + sum(lista2) + sum(lista3)}")

# for i in lista1:
#     print(f'{i}')

# from geradorlista import lista_simples_int

# 1.7 try:

#     posicao = [5,9,10,25]
#     for ident in posicao:

#         print(lista1[ident])
#         print(lista2[ident])
#         print(lista3[ident])

# except IndexError as e:
#     print('continue', ident)

# 1.8 print(len(lista1))
# print(len(lista2))
# print(len(lista3))

# if len(lista1) > len(lista2) and len(lista1) > len(lista3):
#     print('lista 1 é maior')
# elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
#     print('lista 2 é maior')
# else:
#     len(lista3) > len(lista1) and len(lista3) > len(lista2)
#     print('lista 3 é maior')

# 1.9 def subtracao(self, soma_maiores, soma_menores, menor, sub):
#     self.soma_maiores = max(lista1) + max(lista2) + max(lista3)
#     self.soma_menores = min(lista1) + min(lista2) + min(lista3)
#     self.menor = min(soma_menores)
#     self.sub = soma_maiores - soma_menores

#     return (subtracao)
# print(subtracao)
    

# m1 = max(lista1)
# m2 = max(lista2)
# m3 = max(lista3)

# if m1 > m2 and m1 >m3:
#     m1 = m1
# elif m2 > m1 and m2 > m3:
#     m2 = m2
# elif m3 > m1 and m3 > m2:
#     m3 = m3


# me1 = min(lista1)
# me2 = min(lista2)
# me3 = min(lista3)

# if me1 > me2 and me1 >me3:
#     me1 = me1
# elif me2 > me1 and me2 > me3:
#     me2 = me2
# elif me3 > me1 and me3 > me2:
#     me3 = me3

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas


# listas = [lista1,lista2,lista3]

# for soma in listas:
#     s = max(lista1) + max(lista2) + max(lista3)
#     for sub in listas:
#         su = min(lista1) - min(lista2) - min(lista3)
# print(s + su)


