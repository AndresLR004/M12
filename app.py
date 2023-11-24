from flask import Flask, render_template, request, url_for, redirect, g
from datetime import datetime
import sqlite3, os
from flask_login import current_user, LoginManager, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MNjjFdiiY>rtiur5478962H>Uht'
login_manager = LoginManager(app)

login_manager.login_view = 'login'  

basedir = os.path.abspath(os.path.dirname(__file__)) 

def get_db_connection():
    sqlite3_database_path =  os.path.join(basedir, "database.db")
    con = sqlite3.connect(sqlite3_database_path)
    con.row_factory = sqlite3.Row
    return con


@app.before_request
def before_request():
    g.user = current_user 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ver_layout')
def ver_layout():
    return render_template('layout.html')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/products/list', methods=['GET'])
def items_list():
    with get_db_connection() as con:
        res = con.execute("SELECT id, title, description, photo, price, created, updated FROM products")
        items = res.fetchall()
    return render_template('product/list.html', items=items)

@app.route('/products/update/<int:item_id>', methods = ['POST', 'GET'])
def update_item(item_id):
    if request.method == 'GET':
        with get_db_connection() as con:
            res = con.execute("SELECT id, nom, unitats FROM items WHERE id = ?", (item_id, ))
            item = res.fetchone()
            
            if item is None:
                return render_template('error.html', message='Item not found')

        return render_template('product/update.html', item=item)

    else: 
        nom = request.form['nom']
        unitats = int(request.form['unitats']) 

        with get_db_connection() as con:
            con.execute(
                "UPDATE items SET nom = ?, unitats = ? WHERE id = ?", 
                (nom, unitats, item_id)
            )
        return redirect(url_for('product/items_list'))   

@app.route('/products/create', methods=['GET', 'POST'])
def create_item():
    if request.method == 'GET':
        return render_template('product/create.html')
    elif request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        photo = request.form['photo']
        price = float(request.form['price']) 

        created = updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with get_db_connection() as con:
            con.execute(
                "INSERT INTO products (title, description, photo, price, created, updated) VALUES (?, ?, ?, ?, ?, ?)",
                (title, description, photo, price, created, updated)
            )
        
        return redirect(url_for('items_list'))

@app.route('/products/read/<int:product_id>')
def read_item(product_id):
  
    with get_db_connection() as con:
        res = con.execute("SELECT id, title, description, photo, price, created, updated FROM products WHERE id = ?", (product_id,))
        product = res.fetchone()
    if product is None:
        return "El producto no se encontró en la base de datos", 404
    return render_template('product/read.html', product=product)

@app.route('/products/delete/<int:item_id>', methods=['GET', 'POST'])
def delete_item(item_id):
    if request.method == 'GET':
        with get_db_connection() as con:
            res = con.execute("SELECT id, title, description, photo, price, created, updated FROM products WHERE id = ?", (item_id,))
            product = res.fetchone()

            product = res
    if product is None:
            return "El producto no se encontró en la base de datos", 404

    return render_template('product/delete.html', product=product)


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')

class User(UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Lógica de autenticación aquí
        return redirect(url_for('index'))
    return render_template('login.html', title='Log In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Lógica de registro aquí
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)
@app.route('/logout', methods=['GET', 'POST'], endpoint='auth.logout')
def logout():
    # Código para cerrar sesión
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
    # login_manager.init_app(app)
    app.run(debug=True)