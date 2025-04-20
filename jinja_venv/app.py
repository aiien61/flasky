from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    if not name:
        abort(404)
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

# @app.route('/')
# def index():
#     mydict: dict = {'key': 'PA$$W0RD'}
#     mylist: list = [1001, 1002, 1003]
#     return render_template('index.html', mydict=mydict, mylist=mylist)

# @app.route('/user/<name>')
# def user(name):
#     user: str = None
#     if name in {'allen', 'billy'}:
#         user = name
#     return render_template('user.html', user=user)

# @app.route('/comment')
# def comment():
#     comments = ['hello', 'world', 'this', 'is', 'python']
#     return render_template('comment.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)