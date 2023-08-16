#!/usr/bin/python3
"""Starts a Flask web app.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """Ends the current session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns a HTML page with a list of states
    """
    return render_template("7-states_list.html",
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
