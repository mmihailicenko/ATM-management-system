from flask import Flask, render_template, jsonify, abort, request

from model import fetch_atms, fetch_atm, NotFoundError

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/atms')
def all_atms():
    return render_template('index.html', atms=fetch_atms())


@app.route('/atm/<atm_id>')
def get_atm(atm_id):
    try:
        return render_template('atm.html', atm=fetch_atm(atm_id))
    except NotFoundError:
        abort(404, description="Page not found")
