'''
Ejercicio:
2. Usa for en Jinja para mostrar una lista de products.
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/products/list/')
def products():

    # Diccionario con productos
    product1 = {'nombre':'product1', 'descripcion':'descripcion 1', 'precio': 30}
    product2 = {'nombre':'product1', 'descripcion':'descripcion 2', 'precio': 25}
    product3 = {'nombre':'product1', 'descripcion':'descripcion 3', 'precio': 15}
    product4 = {'nombre':'product1', 'descripcion':'descripcion 4', 'precio': 45}

    # Lista de productos
    products = [product1, product2, product3, product4]
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)