from flask import request
from flask import render_template
import pprint
import json
from app import app


@app.route('/')
def my_form():
    return render_template("my-form.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    pretty_json = prettify_json(text)
    return render_template("my-form.html", pretty_json=pretty_json)


def prettify_json(text):
    data = json.loads(str(text))
    return pprint.pformat(data, indent=4, width=10)
    # return eval(text)


if __name__ == '__main__':
    app.run()
