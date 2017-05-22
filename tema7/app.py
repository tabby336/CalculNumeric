#!/usr/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for, json
import json
from solve import *

import random
 
app = Flask(__name__, static_url_path = "", static_folder = "static")

function_values = []
coeffs = []

@app.route('/', methods = ['GET'])
def root():
    return app.send_static_file('index.html')

@app.route('/parameters', methods = ['POST'])
def parameters():
    global coeffs
    data = request.json
    lower = float(data["lower"])
    upper = float(data["upper"])
    num = int(data["num"])
    coeffs = [int(n) for n in data["function"].split()]
    coeffs = [1, -12, 30, 0 ,12]
    coeffs = coeffs[::-1] # reverse coeffs to help at function calculation


    function_values = [(lower, calculate_polynomial_value(coeffs, lower)),(upper, calculate_polynomial_value(coeffs, upper))] # empty the values from last request
    _values = [lower,upper]
    while len(function_values) != num:
        x = random.uniform(lower, upper)
        if x not in _values:
            function_values.append((x, calculate_polynomial_value(coeffs, x)))
            _values.append(x)

    function_values.sort(key = lambda k: k[0])
    solve(function_values)

    return jsonify(function_values)

@app.route('/lagrange', methods = ['POST'])
def lagrange():
    # global y
    data = request.json
    value = json.loads(data)["value"]

    
    fx = approximate_lagrange(value)
    print "\n\n\nPAAAM"
    print fx - calculate_polynomial_value(coeffs, float(value))
    return str(approximate_lagrange(value))

    # return "blaa"

if __name__ == '__main__':
    app.run(debug = True)