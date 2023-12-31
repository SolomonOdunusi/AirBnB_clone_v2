#!/usr/bin/python3
"""Create a Flask app 
that listens on port 5000"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Display a Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
