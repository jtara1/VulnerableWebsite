from flask import request, render_template
import pprint
import json
from app import app


@app.route('/')
def main():
    """ Starting point when the web app is loaded """
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
    # Vulnerability 1
    data = exec(text)
    # data = json.loads(text.replace("'", '"'))  # this alternative would fix Vulnerability 1
    return pprint.pformat(data, indent=4, width=5)
