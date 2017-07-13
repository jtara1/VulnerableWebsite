from flask import request, render_template
import pprint
import json
import os
from app import app


@app.route('/')
def main():
    """ Starting point & home webpage for the web app """
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def input_handler():
    """ Takes input from user """
    text = request.form['text']
    pretty_json = prettify_json(text)
    return render_template("index.html", pretty_json=pretty_json)


def prettify_json(text):
    """ Take some arbitrary string and convert it such that
    string -> python data structure -> readable string representation
    """
    # Vulnerability 2
    data = eval(text)
    # data = json.loads(text.replace("'", '"'))  # this alternative would fix Vulnerability 2
    return pprint.pformat(data, indent=4, width=70)
