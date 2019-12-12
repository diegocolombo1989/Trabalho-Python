# while bole:
    # n = n + 1
    # print(f'Ola Turma {n}')




# while n <= 30:
#     n = n + 1
#     print('Ola Turma')
#     break
# print('Passou!')

# while n <= 20:
#     n = n + 1
#     print(f'Ola Turma {n}')
#         continue
#     print('Passou')



from random import randint
sorteio = randint(1,10)

numero = 0

while not numero == sorteio:
    numero = int(input('Digite um número para ser sorteado: '))
    if numero > sorteio:
        print('O número é maior')
    elif numero < sorteio:
        print('O número é menor')
    else:
        print('Você acertou')
