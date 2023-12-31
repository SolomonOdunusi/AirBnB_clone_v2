#!/usr/bin/python3
"""Create a Flask app 
that listens on port 5000"""
from flask import Flask, render_template
from flask import abort

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Display a Hello HBNB!"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display a HBNB"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display a C <text>"""
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Display a Python <text>"""
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Display a n is a number"""
    if n.isdigit():
        return f"{n} is a number"
    else:
        abort(404)

@app.route('/number_template/<n>', strict_slashes=False)
def num_temp(n):
    """Display a HTML page"""
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
