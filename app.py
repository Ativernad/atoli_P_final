from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Безпечний секретний ключ

# Меню з емодзі (без фото тому що серед нас дехто іх не снайшов)
menu = [
    {"name": "Пательня Креветок", "price": 250, "icon": "🍤"},
    {"name": "Кальмари гриль", "price": 200, "icon": "🦑"},
    {"name": "Суп з морепродуктів", "price": 180, "icon": "🍲"},
    {"name": "Лосось на грилі", "price": 300, "icon": "🐟"},
    {"name": "Кола", "price": 50, "icon": "🥤"},
    {"name": "Мідії в соусі", "price": 220, "icon": "🦪"}
]
@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_name = request.form.get('item_name')
    if item_name and item_name in [item['name'] for item in menu]:
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(item_name)
        session.modified = True
        flash(f'Додано "{item_name}" до кошика!', 'success')
    else:
        flash('Невірний товар!', 'danger')
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart=cart_items, menu=menu)

@app.route('/remove_from_cart/<item_name>')
def remove_from_cart(item_name):
    if 'cart' in session and item_name in session['cart']:
        session['cart'].remove(item_name)
        session.modified = True
        flash(f'Видалено "{item_name}" з кошика!', 'success')
    return redirect(url_for('cart'))

@app.route('/order', methods=['POST'])
def order():
    item_name = request.form.get('item_name')
    if item_name and item_name in [item['name'] for item in menu]:
        flash(f'Ваше замовлення на "{item_name}" прийнято!', 'success')
    else:
        flash('Невірний товар!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)