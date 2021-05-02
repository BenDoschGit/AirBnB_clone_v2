#!/usr/bin/python3
"""Module for running the AirB&B clone project using flask"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False
from models import storage
from models.state import State

@app.route('/cities_by_states')
def states_list():
    states_list = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states_list)

@app.teardown_appcontext
def teardown(filler):
    """closes current SQLAlchemy instance"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
