import math
import random


class SparseMatrix:
  def __init__(self, number_of_lines, values, type = 0):
    if type == 0:
      values = sorted(values, key=lambda x: x[0] * 1000000 + x[1])
      self.number_of_lines = number_of_lines
      self.values = []
      self.is_sparse_matrix = True
      j = 0
      for i in range(self.number_of_lines):
        if i != 0 or i == 0 and values[0][1] != 0:  #nu avem valoare diferita de 0 pe 0 0
          self.values.append((i, -i, 0))
        number_of_elements_on_current_line = 0
        while j < len(values) and values[j][0] == i:
          self.values.append(values[j])
          j += 1
          number_of_elements_on_current_line += 1
        if number_of_elements_on_current_line > 10:
          self.is_sparse_matrix = False
      self.values.append((number_of_lines, -number_of_lines, 0))
      self.number_of_elements = len(self.values)
    else:
      self.number_of_lines = number_of_lines
      self.check_value = check_value

  def get_order_after_columns(self):
    aux = [x for x in self.values if x[1] >= 0]
    aux = sorted(aux, key=lambda x: x[1] * 1000000 + x[0])
    return aux


def read_sparse_matrix(file_name):
  with open(file_name) as f:
    my_lines = f.readlines()
    my_lines = [line.strip() for line in my_lines if len(line.split()) > 0]
  number_of_elements = int(my_lines[0])
  values = [tuple(x.split(", ")) for x in my_lines[1:]]
  values = [(int(x[1]), int(x[2]), float(x[0])) for x in values]
  return SparseMatrix(number_of_elements, values)

def is_sim(a, b, lines):
  a = [x for x in a if x[1] > 0 or (x[1] == 0 and x[2] != 0)]
  b = [x for x in b if x[1] > 0 or (x[1] == 0 and x[2] != 0)]
  ja = 0
  jb = 0
  while ja < len(a) and jb < len(b) and a[ja][0] == b[jb][1] and a[ja][1] == b[jb][0] and math.fabs(a[ja][2] - b[jb][2]) < 0.000000001:
    ja += 1
    jb += 1
  return ja == len(a) and jb == len(b);

def generate_vector(n):
  random.seed(1)
  return [random.randint(1, 9) * 1.0 for i in range(n)]

def euclidian_norm(x):
  norm = 0.0
  for val in x:
    norm += val*val
  return math.sqrt(norm)

def multiply_vector_with_scalar(x, scalar):
  return [val * scalar for val in x]

def multiply_matrix_vector(A, b, n):
  ia = 0
  sol = []
  elem = 0
  while ia < len(A):
    if (A[ia][1] < 0):
      sol.append(elem)
      elem = 0
    else:
      elem += A[ia][2] * b[A[ia][1]];
    ia += 1
  return sol

def dot_prod(a, b):
  rez = 0
  for i in range(len(a)):
    rez += a[i] * b[i];
  return rez

def vector_diff(a, b):
  return [a[i] - b[i] for i in range(len(a))]

def solution():
  A = read_sparse_matrix("m_rar_sim_2017.txt")
  # print(matrix.values[0:10])
  # print(matrix.get_order_after_columns()[0:10])
  if (is_sim(A.values, A.get_order_after_columns(), A.number_of_lines)): 
    x = generate_vector(A.number_of_lines)
    v = multiply_vector_with_scalar(x, 1.0 / euclidian_norm(x))
    w = multiply_matrix_vector(A.values, v, A.number_of_lines)
    lambda_value = dot_prod(w, v)
    k = 0
    k_max = 1000
    eps = 0.00001
    print (A)
    while (euclidian_norm(vector_diff(w, multiply_vector_with_scalar(v, lambda_value))) > A.number_of_lines * eps and k < k_max):
      v = multiply_vector_with_scalar(w, 1.0 / euclidian_norm(w))
      w = multiply_matrix_vector(A.values, v, A.number_of_lines)
      lambda_value = dot_prod(w, v)
      k += 1
      if (k % 10 == 0):
        print (euclidian_norm(vector_diff(w, multiply_vector_with_scalar(v, lambda_value))))
    print (k)
    print (lambda_value)
    # print(multiply_matrix_vector([(0, 0, 3), (0,1,1), (1, -1, 0), (1, 1, 2)], [1, 2], 1))
  else:
    print("nu e simterica")

solution()
