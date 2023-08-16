#!/usr/bin/python3
"""Starts a Flask web app"""
from flask import Flask, render_template
from models import States, storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closing(var=None):
    """Ends the current session"""
    storage.close()

@app.route("/states_list")
def stateList():
    """Returns an html page displaying a list of states"""
    return render_template("7-states_list.html", statess=storage.all(State).values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
