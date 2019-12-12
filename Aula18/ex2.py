
# A lista está organizada da seguinte forma:
#       A primeira lista é o cabeçalho que diz o que siguinifica cada lista a seguir. Ex: Lista de frutas, lita de verduras
#       lista de legumes.
# Com isso responda as seguintes questões:


# print('1: imprima a lista cabeçalho e mostre todos os seus elemantos')

# print('2: imprima a lista verduras e mostre todos os seus elemantos')

# print('3: imprima com f-string a seguinte sequência: abacaxi - laranja - maçã - vergamota')

# print('4: imprima com f-string a seguinte sequência: alface lisa - salsinha - rucula - alface crespa')

# print('5: imprima com f-string a seguinte sequência: frutas: laranja e prera - verduras: repolho e rucula'
#       '\nlegumes: ervilha, feijão branco e grão de bico')

# print('6: imprima com f-string a seguinte sequência: mamão - ervilha, rucula, salsinha, mamão, repolho')

# print('7: imprima com f-string a seguinte sequência: fruta: 3kg de laranja, 8kg de uva, 4.5kg de maçã, 1kg de vergamota')

# print('8: imprima com f-string a seguinte sequência: verduras: 5 maço de salsinha, 4 pés de alface crespa e alface lisa'
#       '2 cabeças de repolho')

# print('9: imprima com f-string a seguinte sequência: legumes: 1kg de feijão, 2kg de gão de bico, 1.5 kg dde soja,'
#       '1 pacote de ervilha')

# print('10: imprima a lista legumes e mostre todos os seus elemantos')

lista = [
          ['frutas','verduras','legumes'],
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
          ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha',],
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja']
        ]

# 1
# cabecalho = [lista[0], lista[1], lista [2]]

# print(cabecalho)

# 2
# print(lista[2])           

# 3                                 abacaxi - laranja - maçã - vergamota
#print(f'{lista[1][1:3]} - {lista[1][5:7]}')

# 4                                 alface lisa - salsinha - rucula - alface crespa
#print(f'{lista[2][1]} - {lista[2][5]} - {lista[2][2]} - {lista[2][0]}')

# 5   frutas: laranja e prera - verduras: repolho e rucula' legumes: ervilha, feijão branco e grão de bico')
#print(f'frutas: {lista[1][2]} e {lista[1][4]} - verduras: {lista[2][5]} e {lista[2][2]} - legumes: {lista[3][1]},{lista[3][4]} e {lista[3][5]}')

# 6                              mamão - ervilha, rucula, salsinha, mamão, repolho
#print(f'{lista[1][0]} - {lista[3][1]} - {lista[2][2]} - {lista[2][5]} - {lista[1][0]} - {lista[2][4]}')

# 7                              fruta: 3kg de laranja, 8kg de uva, 4.5kg de maçã, 1kg de vergamota
#print(f'3kg de {lista[1][2]}, 8kg de {lista[1][3]}, 4.5kg de {lista[1][5]}, 1kg de {lista[1][6]}')

# 8                              verduras: 5 maço de salsinha, 4 pés de alface crespa e alface lisa 2 cabeças de repolho
#print(f'5 maço de {lista[2][5]}, 4 pés de {lista[2][0]} e {lista[2][1]}, 2 cabeças de {lista[2][4]}')

# 9                            legumes: 1kg de feijão, 2kg de gão de bico, 1.5 kg dde soja, 1 pacote de ervilha
#print(f'legumes: 1kg de {lista[3][0]}, 2kg de {lista[3][6]}, 1.5kg de {lista[3][6]}, 1 pacote de {lista[3][1]}')

# 10                           
#print(lista[3:])