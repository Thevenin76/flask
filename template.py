'''
Ejercicio:
1. Agrega un if en el template que muestre "Eres administrador" si el usuario es "admin".
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/usuario/<nombre>')
def usuario(nombre):

    if (nombre == 'admin'):
        return render_template('index.html', nombre=nombre, eres_admin='eres_admin')
     
    return render_template('index.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)