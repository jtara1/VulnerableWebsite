from flask import Flask
from flask import request
from flask import render_template
import pprint

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("my-form.html")


@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = text.upper()
    return processed_text


def prettify_json(text):
    pp = pprint.PrettyPrinter(indent=4)
    json = eval(text)
    pp.pprint(json)


if __name__ == '__main__':
    app.run()