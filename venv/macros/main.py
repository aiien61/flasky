from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "iPhone", "brand": "Apple", "price": 25000, "stock": 0},
    {"name": "MacBook", "brand": "Apple", "price": 55000, "stock": 10},
    {"name": "Galaxy Note", "brand": "Samsung", "price": 20000, "stock": 5},
    {"name": "Galaxy Tab", "brand": "Samsung", "price": 18000, "stock": 0},
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run()
