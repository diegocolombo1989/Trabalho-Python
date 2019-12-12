# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com


# 2 - usando o for, imprima todos nomes um abaixo do outro
#
# 3 - Usando a indexação faça uma lista com 3 dicionarios contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)

# campos = ('nome', 'telefone', 'email', 'idade')

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                 'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                 'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                 'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                 ]


dados = ('nome', 'email', 'idade', 'telefone')

dic1 = cadastroHBSIS[1][3]
dic2 = cadastroHBSIS[1][1]
dic3 = cadastroHBSIS[1][5] 

lista1 = dic1,dic2,dic3

for lista in dados,lista1:
    print(lista)