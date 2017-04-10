import random
import numpy as np

def generate_simetric_matrix(n):
  random.seed(10)
  matrix = [[0 for j in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(i):
      matrix[i][j] = matrix[j][i]
    for j in range(i, n):
      matrix[i][j] = random.randint(1, 9)
  return np.array(matrix)

def generate_vector(n):
  random.seed(1)
  return np.array([random.randint(1, 9) for i in range(n)])

def euclidian_norm(v):
  return np.linalg.norm(v)

# print(np.dot(x, y))
# print(y*10)
# n=3
# A = generate_simetric_matrix(n)
# x = generate_vector(n)
# print(A)
# print(x)
# print(np.dot(A,x))


def solution(n):
  A = generate_simetric_matrix(n)
  x = generate_vector(n)
  v = x / euclidian_norm(x)
  w = np.dot(A, v)
  lambda_value = np.dot(w, v)
  k = 0
  k_max = 1000
  eps = 0.00001
  print (A)
  while (euclidian_norm(w - lambda_value * v) > n * eps and k < k_max):
    v = w * (1/euclidian_norm(w)) 
    w = np.dot(A, v)
    lambda_value = np.dot(w, v)
    k += 1
    # print ("**************")
    # print (euclidian_norm(w - lambda_value * v))
    # print (v)
    # print (w)
  print (k)
  print (lambda_value)

solution(4)




