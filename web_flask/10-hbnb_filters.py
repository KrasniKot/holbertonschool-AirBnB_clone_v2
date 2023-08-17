#!/usr/bin/python3
"""Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def states():
    """Returns an html page
    """
    return render_template("10-hbnb_filters.html",
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())


@app.teardown_appcontext
def storage_close(arg=None):
    """Ends the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
