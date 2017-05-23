import random
import numpy as np

EPS = 0.000000001

def generate_simetric_matrix(n):
  random.seed(10)
  matrix = [[0 for j in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(i):
      matrix[i][j] = matrix[j][i]
    for j in range(i, n):
      matrix[i][j] = random.randint(1, 9)
  return np.array(matrix)


def generate_sparse_matrix():
  import scipy.sparse as sparse
  print sparse.rand(10, 10, density=0.1)


def generate_vector(n):
  random.seed(1)
  return np.array([random.randint(1, 9) for i in range(n)])

def euclidian_norm(v):
  return np.linalg.norm(v)


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


def single_value(a):
  U, S, V = np.linalg.svd(a, full_matrices=True)
  return [x for x in S if x > -EPS]

def rang(a):
  single_values = single_value(a)
  return len([x for x in single_values if abs(x) > EPS])

def conditional_number(a):
  single_values = single_value(a)
  return max(single_values)/min([x for x in single_values if abs(x) > EPS])

def norm(a):
  U, S, V = np.linalg.svd(a, full_matrices=True)
  b = np.zeros(shape=a.shape)
  for i in range(min(a.shape)):
    b[i][i] = S[i]
  sol = (U*b*V)
  # print(a.item(1,1))
  infinit_norm = -1
  for i in range(a.shape[0]):
    for j in range(a.shape[1]):
      infinit_norm = max([infinit_norm, abs(sol.item((i, j)) - a.item((i, j)))])
  return infinit_norm

def get_column(a, i):
  return a.transpose()[i].transpose()

def compute_As(a, s):
  # print("In matricea a ", rang(a))
  if (rang(a) <= s):
    return None
  U, S, V = np.linalg.svd(a, full_matrices=True)
  As = np.zeros(shape=a.shape)
  # print(a)
  for i in range(s):
    u = get_column(U, i)
    v = get_column(V, i).transpose()
    As +=  S[i] * u * v
  return As



# a = np.matrix([[1, 2, 3], [100, 200, 6], [1, 2, 9]])
# print("Valori singulare: ", single_value(a))
# print("Rang matrice: ", rang(a))
# print("Numar de conditionare: ", conditional_number(a))
# print("Norma infinit: ", norm(a))
# print(compute_As(a, 2))
