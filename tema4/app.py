#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for
import tema4

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/', methods=['GET'])
def root():
  return app.send_static_file('index.html')


@app.route('/info/<matrix>', methods=['GET'])
def info(matrix):
  print(matrix)
  info = tema4.find_solution(matrix)
  if (info["nr_iteration"] == 9999):
    return jsonify (
      time = info["time"],
      isSol = False
    )
  return jsonify(
    isSol = True,
    error = info["error"],
    time = info["time"],
    iter = info["nr_iteration"]
  )


if __name__ == '__main__':
  app.run(debug=True)
