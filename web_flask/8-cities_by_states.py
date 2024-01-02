#!/usr/bin/python3
"""Create a Flask app
that listens on port 5000"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state():
    """Display a HTML page"""
    states = storage.query(State).order_by(State.name).all()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the current db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
