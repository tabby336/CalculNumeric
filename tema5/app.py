#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
 
app = Flask(__name__, static_url_path = "", static_folder = "static")

import inverse
import utils

def default_answer(method):
    data = inverse.calculate_inverse(inverse.matrix, method)
    if isinstance(data[0], basestring):
        return jsonify({ 'divergent': "Sirul este divergent",
                         'k': data[1] })
    else:
        return jsonify({'k': data[2],
                        'norm': data[1]})

@app.route('/', methods = ['GET'])
def root():
    return app.send_static_file('index.html')

@app.route('/initMatrix', methods = ['GET'])
def init_matrix():
    return jsonify({ 'n': str(inverse.n),
                     'a': utils.matrix_as_string(inverse.matrix) })

@app.route('/schultz', methods = ['GET'])
def schultz():
    return default_answer('schultz')

@app.route('/formula2', methods = ['GET'])
def formula2():
    return default_answer('formula2')

@app.route('/formula3', methods = ['GET'])
def formula3():
    return default_answer('formula3')





if __name__ == '__main__':
    inverse.read_data()
    app.run(debug = True)