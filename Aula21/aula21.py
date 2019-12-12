

# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.
#© 2019 GitHub, Inc.

# controle = 's'
# while controle != 's':

#     n1 = int(input('Digite n1: '))
#     n2 = int(input('Digite n2: '))

#     print(f'A soma do {n1}+ {n2} é: {n1 + n2}')
#     print(f'A divisão do {n1}+ {n2} é: {n1 / n2}')
#     print(f'A multiplição do {n1}+ {n2} é: {n1 * n2}')
#     print(f'A subtração do {n1}+ {n2} é: {n1 - n2}')

#     controle = input("Digite 's' para sair: ")


# try:
#     numero = int(input('Digite um numero: '))
    
# except:
#     print('Voce digitou o numero errado seu tatu: ')

# print('1')
# print('2')

# while True:
#     try:
#         print('Passou 1')
#         numero = int(input('Digite um numero: '))
#         print('Passou 2')
#    except ValueError:
#         print'Voçê digitou o numero errado seu tatu')
#    else:
#         print('Passou1')
#         print('Passou2')



# faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.

# n = -1
# while n != 0:
#     try:
#         n=int(input('Digite um numero inteiro: '))
#     except ValueError:
#         print('Você digitou o numero errado seu tatu')
#     else:
#         print('Muito bem, animal')


#Faça outro tratamento de exceção para evitar que divida um numero
# por zero.





while True:
    try:
        n = int(input('Digite um numero: '))
        n1 = int(input('Digite um numero para ser dividio pelo primeiro: '))
        print(f'Primeiro número digitado = {n} dividido pelo segundo digitado = {n1} é: {n / n1} ')
    except ValueError:
        print('Digite numeros inteiros')

    except ZeroDivisionError:
        print('Não divide por 0')
    else:
        break
