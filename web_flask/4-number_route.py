#!/usr/bin/python3
"""Module for running the AirB&B clone project using flask"""
from flask import Flask
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
    with n is a number, if n is a number"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
