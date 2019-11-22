nome_pagina = 'Calculadora'

from flask import Flask, render_template, request

from aula9_calc import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo=nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = int(request.args['numero1'])
    n2 = int(request.args['numero2'])
    soma1 = soma(n1,n2)
    subtracao1 = subtracao(n1,n2)
    multiplicacao = mult(n1,n2)
    divisao_inteira = div_inteira(n1,n2)
    divisao_fracionada = div_frac(n1,n2)
    resto1 = resto_div(n1,n2)
    raiz1 = raiz(n1,n2)
    resultados = {'soma':soma1, 'subtracao':subtracao1, 'multiplicacao': multiplicacao, 'divisao_inteira':divisao_inteira, 'divisao_fracionada':divisao_fracionada, 'resto': resto1, 'raiz':raiz1}

    return render_template(
        'resultado.html', n1 = n1, n2 = n2, resultados = resultados)

app.run()