#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import puncte_minim
import radacini
import json
 
app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.route('/', methods = ['GET'])
def root():
    return app.send_static_file('index.html')

@app.route('/info1', methods = ['POST'])
def minimum_point1():
    return jsonify({ "result": puncte_minim.get_minimum_point(puncte_minim.der_first, puncte_minim.der2_first)})

@app.route('/info2', methods = ['POST'])
def minimum_point2():
    return jsonify({ "result": puncte_minim.get_minimum_point(puncte_minim.der_second, puncte_minim.der2_second)})

@app.route('/info3', methods = ['POST'])
def minimum_point3():
    return jsonify({ "result": puncte_minim.get_minimum_point(puncte_minim.der_third, puncte_minim.der2_third)})


@app.route('/info4', methods = ['POST'])
def minimum_point4():
    d = json.loads(request.data)["data"]
    rad = radacini.find_roots([int(x) for x in d.split(" ")])
    rad = [str(x) for x in rad]
    return jsonify({ "result": rad })

# @app.route('/schultz', methods = ['GET'])
# def schultz():
#     return default_answer('schultz')

# @app.route('/formula2', methods = ['GET'])
# def formula2():
#     return default_answer('formula2')

# @app.route('/formula3', methods = ['GET'])
# def formula3():
#     return default_answer('formula3')


if __name__ == '__main__':
    app.run(debug = True)