#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
 
app = Flask(__name__, static_url_path = "", static_folder = "static")

import ex, utils
 
@app.route('/', methods = ['GET'])
def root():
    return app.send_static_file('index.html')


@app.route('/choleski', methods = ['GET'])
def choleski():
    a,l,d,lt = utils.get_cholesky_matrices(ex.n, ex.a, ex.d)
    return jsonify( { 'n': str(ex.n), 
                      'a': utils.matrix_as_string(a), 
                      'l': utils.matrix_as_string(l), 
                      'd': utils.matrix_as_string(d), 
                      'lt': utils.matrix_as_string(lt) } )

@app.route('/determinant', methods = ['GET'])
def determinant():
    d = utils.get_determinant_matrix(ex.n, ex.d)
    return jsonify( { 'n': str(ex.n), 
                      'd': utils.matrix_as_string(d), 
                      'det': str(ex.det) } )

@app.route('/solution', methods = ['GET'])
def solution():
    a,l,d,lt = utils.get_cholesky_matrices(ex.n, ex.a, ex.d)
    return jsonify( { 'n': str(ex.n), 
                      'a': utils.matrix_as_string(a),
                      'x': utils.vector_as_string(ex.x), 
                      'b': utils.vector_as_string(ex.b) } )

@app.route('/lu', methods = ['GET'])
def lu():
    return jsonify( { 'P': utils.matrix_as_string(ex.P),
                      'L': utils.matrix_as_string(ex.L),
                      'U': utils.matrix_as_string(ex.U),
                      'n': str(ex.n), 
                      'solution': utils.vector_as_string(ex.lu_sol) } )
    

@app.route('/norm', methods = ['GET'])
def norm():
    a, l, d, lt = utils.get_cholesky_matrices(ex.n, ex.a, ex.d)
    return jsonify( { 'n': str(ex.n), 
                      'a': utils.matrix_as_string(a),
                      'x': utils.vector_as_string(ex.x), 
                      'b': utils.vector_as_string(ex.b),
                      'prod_terms': utils.vector_as_string(ex.ax_terms), 
                      'norm': str(ex.norm) } )

if __name__ == '__main__':
    app.run(debug = True)