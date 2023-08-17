#!/usr/bin/python3
"""Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """Returns an html page
    """
    return render_template("9-states.html",
                           states=storage.all(State).values())


@app.route("/states/<sid>")
def stateCities(sid):
    """Returns an html page
    """
    return render_template("9-states.html",
                           states=storage.all(State).values(), sid=sid)


@app.teardown_appcontext
def storage_close(arg=None):
    """Ends the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
