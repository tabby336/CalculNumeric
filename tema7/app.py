#!/usr/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for, json
import json
from tema7 import *

import random
 
app = Flask(__name__, static_url_path = "", static_folder = "static")

function_values = []
coeffs = []

@app.route('/', methods = ['GET'])
def root():
    return app.send_static_file('index.html')

@app.route('/parameters', methods = ['POST'])
def send_params():
    return jsonify(values(-2,10,4,polinom))


if __name__ == '__main__':
    app.run(debug = True)