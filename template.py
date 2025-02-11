from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template('index.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)