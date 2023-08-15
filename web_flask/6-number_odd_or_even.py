#!/usr/bin/python3
"""Starts a Flask web app"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Displays 'HBNB!'"""
    return "HBNB"


@app.route("/c/<text>")
def cText(text):
    """Returns a text"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python")
@app.route("/python/<text>")
def pythonText(text="is cool"):
    """Returns a text"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>")
def number(n):
    """Returns only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def numberTemplate(n):
    """Returns an html page"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def evenSo(n):
    """Returns an html page depending on the parity of n"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
