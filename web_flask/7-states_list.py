#!/usr/bin/python3
"""Module for running the AirB&B clone project using flask"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False
from models import storage
from models.state import State

@app.route('/states_list')
def states_list():
    states_list = storage.all("State").values()
    for state in states_list:
        if isinstance(state, State):
            state = state.to_dict()
    return render_template("7-states_list.html", states=states_list)

@app.teardown_appcontext
def teardown(filler):
    """closes current SQLAlchemy instance"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
