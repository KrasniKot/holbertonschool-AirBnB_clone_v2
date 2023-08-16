#!/usr/bin/python3
"""Starts a Flask web application.
"""
from models import storage, States
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all States

    ..sorted by name.
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(args):
    """Ends the current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
