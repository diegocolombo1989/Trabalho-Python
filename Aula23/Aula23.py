# For para dicionário

dias_cada_mes= {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

# qual_mes = int(input('Digite o número do mês (1...12): '))


# print(sum(list(dias_cada_mes.values())[qual_mes-1:]))

# total = 0
# for mes in range(qual_mes, 12+1):
#     total += dias_cada_mes[mes]
# print('modo estruturado')
# print('total de dias ate o final do ano', total)

for chave in dias_cada_mes:
    print('Tenho uma chave nessa linha', chave)
    print('Se tenho a chave, tenho o valor', dias_cada_mes [chave])

for chave, valor in dias_cada_mes.items():
    print('Para a chave', chave, 'o valor', valor)

tupla = ('Texto', 'texto de novo', 'textei', 'textamento')
for isto in tupla:
    print(type(isto))
    print(isto)


