# Exercicio 3 foreach
# Escreva programa que leia as notas (4) de 10 alunos
# Armazene os nomes na lista
# Imprima:
# 1 O nome dos alunos
#   1- o nome dos alunos
#   2- Média do aluno
#   3- Resultado ( Aprovado >= 7.0)


lista = []

for i in range(0,10):
    
    lista.append(input('Digite seu nome: '))
    n1 = float(input(' digite nota 1: '))
    n2 = float(input(' digite nota 2: '))
    n3 = float(input(' digite nota 3: '))
    n4 = float(input(' digite nota 4: '))
    media = float(F'{(n1 + n2 + n3 + n4) / 4}')
    print('media: ', media)
    if media >= 7.0:
        print('Aprovado')
    else:
        print('Reprovado')
    print(lista)
