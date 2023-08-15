#!/usr/bin/python3
"""Starts a Flask web app"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
