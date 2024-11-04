from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    user: str = None
    if name in {'allen', 'billy'}:
        user = name
    return render_template('user.html', user=user)

@app.route('/comment')
def comment():
    comments = ['hello', 'world', 'this', 'is', 'python']
    return render_template('comment.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)