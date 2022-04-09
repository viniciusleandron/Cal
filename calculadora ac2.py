import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('calculadoraweb.html')


@app.route('/calcule', methods=['POST', 'GET'])
def calcule():
    valor1 = request.form['num1']
    valor2 = request.form['num2']
    operacao = request.form['operacao']
    num1 = float(valor1)
    num2 = float(valor2)

    if operacao == 'somar':
        resultado = num1 + num2
    elif operacao == 'subtrair':
        resultado =  num1 - num2
    elif operacao == 'multiplicar':
        resultado =  num1 * num2
    elif operacao == 'divisao':
        if  num1 == 0 or num2 == 0:
            resultado = "Erro divisao por 0"
        else:
            resultado = num1 / num2
    return str(f'O total é: {resultado}')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
