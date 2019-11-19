# Crie um programa que:
# 1- Leia dois numeros inteiros
# 2- Calcule a soma entre os dois numeros atraves de um metodo
# 3- Calcule a subtração entre os dois numeros atraves de um metodo
# 4- Calcule a multiplicação entre os dois numeros atraves de um metodo
# 5- Calcule a divisão inteira entre os dois numeros atraves de um metodo
# 6- Calcule a sdivisão fracionado entre os dois numeros atraves de um metodo
# 7- Calcule resto da divisão entre os dois numeros atraves de um metodo
# 8- Calcule a raiz entre os dois numeros atraves de um metodo
# 9- Separa os metodos em outro arquivo


from aula9_calc import soma, subtracao, mult, div_inteira, div_frac, resto_div, raiz


n1 = int( input('Digite numero 1:'))
n2 = int( input('Digite numero 2:'))



print(f'Soma dos numeros: { soma(n1,n2) } ')
print(f'Subtração dos numeros: { subtracao(n1,n2) } ')
print(f'Multiplicação dos numeros: { mult(n1,n2) } ')
print(f'Divisão inteira dos numeros: { div_inteira(n1,n2) } ')
print(f'Divisão fracionada dos numeros: { div_frac(n1,n2) } ')
print(f'Resto da divisão dos numeros: { resto_div(n1,n2) } ')
print(f'Raiz quadrada entre os dois numeros: { raiz(n1,n2) } ')