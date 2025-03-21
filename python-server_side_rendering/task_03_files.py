from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    """Lire et retourner les données depuis le fichier JSON."""
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv():
    """Lire et retourner les données depuis le fichier CSV."""
    products = []
    with open('products.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['id'] = int(row['id'])  # Convertir l'ID en entier
            row['price'] = float(row['price'])  # Convertir le prix en float
            products.append(row)
    return products

@app.route('/products')
def products():
    # Obtenir les paramètres de l'URL
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Vérifier le paramètre 'source' et lire les données
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtrer les produits si un id est fourni
    if product_id:
        filtered_products = [product for product in products if product['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
