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
	data = request.get_json()
	data["lower"] = float(data["lower"])
	data["upper"] = float(data["upper"])
	data["num"] = int(data["num"])
	coef = [float(x) for x in data["function"].split(" ")]
	coef.reverse();
	data["function"] = coef
	print("***************")
	print(data)
	print("***************")
	return jsonify(values(data["lower"], data["upper"], data["num"], data["function"]))

@app.route('/lagrange', methods = ['POST'])
def lagrange():
	data = request.get_json()
	data["lower"] = float(data["lower"])
	data["upper"] = float(data["upper"])
	data["num"] = int(data["num"])
	data["value"] = float(data["value"])
	coef = [float(x) for x in data["function"].split(" ")]
	coef.reverse();
	data["function"] = coef
	print("***************")
	print(data)
	print("***************")
	return jsonify({"value":compute_value(data["value"], data["lower"], data["upper"], data["num"], data["function"])})

@app.route('/periodic', methods = ['POST'])
def periodic():
	return jsonify(grafic_b(0, 31 * math.pi / 16, 20, second_periodic))

@app.route('/periodicCompute', methods = ['POST'])
def periodicCompute():
	value = request.get_json()["value"]
	print(value)
	return jsonify({"value": solve_b(float(value), 0, 31 * math.pi / 16, 20, second_periodic)})

if __name__ == '__main__':
    app.run(debug = True)