
# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igual a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
#
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)


cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                 'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                 'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                 'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                 ]

cab = cadastroHBSIS[0::2]

dados = cadastroHBSIS[1::2]

for nome in cab,dados:
   print(nome)
