from flask import Flask, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400

@app.route('/user/<name>')
def user(name: str):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/blog')
def blog():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/google')
def google():
    return redirect('https://www.google.com')


def load_user(id: int):
    users: dict = {1: 'Allen', 2: 'Billy', 3: 'Carter'}
    return users.get(id)

@app.route('/user/<int:id>')
def get_user(id: int):
    user = load_user(id)
    if not user:
        abort(404)
    return f'<h1>Hi, {user}</h1>'

if __name__ == '__main__':
    app.run(debug=True)