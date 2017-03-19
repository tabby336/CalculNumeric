#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for
import sparseMatrix

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/', methods=['GET'])
def root():
  return app.send_static_file('index.html')


@app.route('/sum', methods=['GET'])
def sum():
  a = sparseMatrix.read_sparse_matrix("a.txt")
  b = sparseMatrix.read_sparse_matrix("b.txt")
  expected_result = sparseMatrix.read_sparse_matrix("aplusb.txt")
  result = sparseMatrix.add_sparse_matrix(a, b)
  if result is None:
    return jsonify(
      result="The provided matrixes are not sparse matrix."
    )
  if sparseMatrix.equal_matrixes(result, expected_result):
    return jsonify(
      result=True
    )
  else:
    return jsonify(
      result=False
    )


@app.route('/productVector', methods=['GET'])
def productVector():
  matrix = request.args.get('param')
  a = sparseMatrix.read_sparse_matrix(matrix + '.txt')
  result = sparseMatrix.multiply_sparse_matrix_with_a_vector(a)
  if result is None:
    return jsonify(
      result="The provided matrixes are not sparse matrix."
    )
  if sparseMatrix.equal_vectors(result, a):
    return jsonify(
      result=True
    )
  else:
    return jsonify(
      result=False
    )


@app.route('/product', methods=['GET'])
def product():
  a = sparseMatrix.read_sparse_matrix("a.txt")
  b = sparseMatrix.read_sparse_matrix("b.txt")
  expected_result = sparseMatrix.read_sparse_matrix("aorib.txt")
  result = sparseMatrix.sparse_matrix_multiplication(a, b)
  x = sparseMatrix.equal_matrixes(result, expected_result)
  if result is None:
    return jsonify(
      result="The provided matrixes are not sparse matrix."
    )
  if x:
    return jsonify(
      result=True
    )
  else:
    return jsonify(
      result=False
    )


if __name__ == '__main__':
  app.run(debug=True)
