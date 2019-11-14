nota1 = float(input('Digite nota 1: '))
nota2 = float(input('Digite nota 2: '))
nota3 = float(input('Digite nota 3: '))
nota4 = float(input('Digite nota 4: '))

#lista = [nota1, nota2, nota3, nota4]
#print('A maior nota foi:', max(lista))
#print('A menor nota foi:', min(lista))

if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
    print(f'A maior nota é a {nota1}')
elif nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
    print(f'A maior nota é a {nota2}')
elif nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
    print(f'A maior nota é a {nota3}')
else:
    print(f'A maior nota é a {nota4}')
  
if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    print(f'A menor nota é a {nota1}')
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    print(f'A menor nota é a {nota2}')
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    print(f'A menor nota é a {nota3}')
else:
    print(f'A menor nota é a {nota4}')
  
  
  
media = (nota1 + nota2 + nota3 + nota4) / 4
    
print('Média do aluno: media:', media)
if media >= 7.0:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')



    ('-'*50)