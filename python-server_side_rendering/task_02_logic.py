from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Lire les données JSON depuis le fichier
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []

    # Passer la liste des éléments au template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True)
