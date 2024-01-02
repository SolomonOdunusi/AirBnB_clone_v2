#!/usr/bin/python3
"""Create a Flask app
that listens on port 5000"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state():
    """Display a HTML page"""
    states = sorted(storage.all("State").values())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the current db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
