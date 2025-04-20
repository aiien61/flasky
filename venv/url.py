from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello World!</h1>'

@app.route("/user/<name>")
def user(name):
    print(type(name))
    return f'<h1>Hello, User {name}!</h1>'

@app.route("/uid/<int:id>")
def uid(id):
    print(type(id))
    return f'<h1>User ID: {id}!</h1>'

@app.route("/account/<string:acct>")
def account(acct):
    print(type(acct))
    return f'<h1>Account: {acct}!</h1>'

@app.route("/score/<float:point>")
def score(point):
    print(type(point))
    return f'<h1>Score: {point}</h1>'

@app.route("/link/<path:url>")
def link(url):
    print(type(url))
    return f'<h1>Link: {url}</h1>'

if __name__ == "__main__":
    app.run()