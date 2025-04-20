from flask import Flask, render_template
import json

app = Flask(__name__)

data = {
    "products": ['iPhone', 'Samsung Galaxy'],
    "brands": ["apple", "samsung"],
    "prices": [25_000, 12_000],
    "discounts": [0.11, 0.35],
    "stocks": [-100, 10],
    "desc": [
        '    apple gives you the best ecosystem   ',
        'have a seamless experience with samsung'
    ],
    "slogans": [
        "Buy <strong>iPhone</strong> now and get <em>10% off</em>!",
        "Buy <strong>Samsung Galaxy</strong> now and get <em>30% off</em>!"
    ]
}

versions = {
    "version": ["iphone13", "iphone14", "iphone15", "iphone16"]
}

products = [
    {"name": "iPhone", "brand": "Apple", "price": 25000, "stock": 0},
    {"name": "MacBook", "brand": "Apple", "price": 55000, "stock": 10},
    {"name": "Galaxy Note", "brand": "Samsung", "price": 20000, "stock": 5},
    {"name": "Galaxy Tab", "brand": "Samsung", "price": 18000, "stock": 0},
]

product_attr = {
    "id": "p1", "class": "featured", "data-price": "1999"
}

class ProductData:
    def __init__(self, data):
        self.products = data['products']
        self.brands = data['brands']
        self.prices = data['prices']
        self.discounts = data['discounts']
        self.stocks = data['stocks']
        self.desc = data['desc']
        self.slogans = data['slogans']


@app.route("/")
def index():
    kwargs = {
        'data': data,
        'data_json': json.dumps(data, indent=2),
        'product_data': ProductData(data),
        'versions': versions,
        'products': products,
        'product_attr': product_attr,
        'line': "<script>alert('Out of Stock!')</script>"
    }
    return render_template('index.html', **kwargs)


if __name__ == "__main__":
    app.run()