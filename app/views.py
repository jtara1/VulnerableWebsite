from flask import request
from flask import render_template
import pprint
import json
import os
import sys
import PIL
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
    string -> json_data_structure -> readable string representation
    """
    data = eval(text)
    # data = json.loads(text.replace("'", '"'))
    return pprint.pformat(data, indent=4, width=5)


if __name__ == '__main__':
    app.run()
