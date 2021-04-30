#!/usr/bin/python3
"""Module for running the AirB&B clone project using flask"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Sets up / to respond to HTTP get requests with Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Sets up /hbnb to respond to HTTP get requests with HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Sets up /c/text to respond to HTTP get requests
    with C follwed by the value of text"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>')
def python_is_fun(text):
    """Sets up /python/text to respond to HTTP get requests
    with Python follwed by the value of text"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number(n):
    """Sets up /number/n to respond to HTTP get requests
    with n is a number, if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Sets up /number/n to respond to HTTP get requests
    with display a HTML page only if n is an integer"""
    return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """Sets up /number/n to respond to HTTP get requests
    with display a HTML page based on if n is odd or even
    only if n is an integer"""
    if n % 2 == 0:
        even = True
    else:
        even = False
    return render_template("6-number_odd_or_even.html", num=n, even=even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
