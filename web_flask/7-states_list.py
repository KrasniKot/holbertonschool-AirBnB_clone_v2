#!/usr/bin/python3
"""Task 7. Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """After each request, remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a HTML page with the list of states
    """
    return render_template("7-states_list.html",
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
