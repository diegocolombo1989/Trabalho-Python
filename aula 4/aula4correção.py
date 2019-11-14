# Leia 2 numero
# Realize as quatro operações
# Imprime o resultado das operações
# Diga qual numero é o maior dos dois numeros

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))

print(f'Soma : {n1} + {n2} =  {n1 + n2}')
print(f'subração : {n1} - {n2} = {n1 - n2}')
print(f'Divisão : {n1} / {n2} = {n1 / n2}')
print(f'Multiplicação : {n1} * {n2} : {n1 * n2}')

if n1 > n2:
    print('numero 1 é maior que numero 2')
else:
    print('numero 2 é maior que numero 1')    