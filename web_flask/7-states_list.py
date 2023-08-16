#!/usr/bin/python3
"""Starts a Flask web application.
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def statesList():
    """Displays an HTML page with a list of all States

    sorted by name.
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tearDown(self):
    """Ends the current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
