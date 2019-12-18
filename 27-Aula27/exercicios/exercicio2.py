# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como default ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
# print(id(lista))
# print(id(embaralhar))

# print(lista is embaralhar)

# 2) Qual é o maior valor destas duas listas 

#print(f'O maior valor das duas listas é: {max(lista[0 or 1])}')


# 3) Qual é o maior valor de cada lista

#print(f'O maior valor da lista 1 é: {max(lista[0])} e o maior valor da lista 2 é: {max(lista[1])}')

# 4) Há o número 10 dentro da lista[0]?

#print(10 in lista[0])

# 5) Há o número 20 dentro da lista[1]?

#print(5 in lista[1])

# 6) Quantos números da lista[0] tem dentro da lista[1]?
# cont = 0

# for i in lista[0]:
#     if i in lista[1]:
#         cont = cont + 1
# print(cont)


# 7) Mostre os números da lista[0] que estão dentro da lista[1]
# quant = 0
# for numeros in lista[0]:
#     if numeros in lista[1]:
#         quant = quant + 1
# print(f"Há {numeros} nas duas listas")

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]

# for mult in lista[0]:
#     soma = sum(lista[0]) 
#     resultado = soma * sum(lista[1])
# print(resultado)

# 9) Faça uma divisão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!

# maior = max(lista[0])
# menor = min(lista[1])

# if maior > menor:
#     resultado = maior // menor
# else: 
#     resultado = menor // maior

# if resultado in lista[0]:
#     print('O resultado esta na lista 1.')
# else:
#     resultado in lista[1]
#     print('O resultado esta na lista 2.')
    



# 10) Ferifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]

# maior = max(lista[0])
# menor = min(lista[1])

# if maior in lista[1]:
#     print('O número maior da lista 1 esta na lista 2.')
# else:
#     print('O numero nao esta aqui')
# if menor in lista[0]:
#     print('O número menor da lista 2 esta dentro da lista 1.')
# else:
#     print('O numero nao esta aqui')
