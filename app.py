'''
Aprendiendo Flask:
https://chatgpt.com/share/67ab19dd-f3e4-8012-becd-74aab31069f1

Santa Cruz de Tenerife Febrero de 2025
Thevenin76
'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Flask!"

@app.route('/about')
def about():
    return "Esta es la página Acerca de"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Hola, {nombre}'

@app.route('/sumar/<a>/<b>', methods=['GET', 'POST'])
def sumar(a, b):
    if request.method == 'POST':        
        return "Procesando un formulario..."
    resultado = int(a)+int(b)
    return f"GET muestra un formulario, pero en este caso simplemente sumamos {resultado}"

@app.route('/multiplicar/<a>/<b>', methods=['GET'])
def multiplicar(a, b):
    resultado = int(a)*int(b)
    return f'{resultado}'


@app.route('/info',  methods=['GET', 'POST'])
def info():
    ''' Para facilidad de uso, en lugar de solo aceptar POST como dice ChatGPT aceptamos solo GET '''
    if request.method == 'GET':
        return 'Esta es la página de información'
    else:
        return 'Método POST no aceptado'
    
if __name__ == '__main__':
    app.run(debug=True)
