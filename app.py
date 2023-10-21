from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/items/list')
def items_list():
    return render_template('list.html')

@app.route("/hola/<nom>")
def hola(nom):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return f"Hola {nom}. La data i hora d'ara mateix és: {formatted_now}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)