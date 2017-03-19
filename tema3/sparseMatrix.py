class SparseMatrix:
  def __init__(self, number_of_lines, values, check_value, type = 0):
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
      self.check_value = check_value
    else:
      self.number_of_lines = number_of_lines
      self.check_value = check_value
      self.values = values

  def get_order_after_columns(self):
    aux = [x for x in self.values if x[1] >= 0]
    aux = sorted(aux, key=lambda x: x[1] * 1000000 + x[0])
    return aux


def read_sparse_matrix(file_name):
  with open(file_name) as f:
    my_lines = f.readlines()
    my_lines = [line.strip() for line in my_lines if len(line.split()) > 0]
  number_of_elements = int(my_lines[0])
  check_value = [float(x) for x in my_lines[1:number_of_elements + 1]]
  values = [tuple(x.split(", ")) for x in my_lines[number_of_elements + 1:]]
  values = [(int(x[1]), int(x[2]), float(x[0])) for x in values]
  return SparseMatrix(number_of_elements, values, check_value)


def compare(first, second):
  if first[0] * 10000000 + first[1] < second[0] * 10000000 + second[1]:
    return 1
  elif first[0] * 10000000 + first[1] == second[0] * 10000000 + second[1]:
    return 0
  else:
    return 2


def add_sparse_matrix(a_matrix, b_matrix):
  if not a_matrix.is_sparse_matrix or not b_matrix.is_sparse_matrix:
    return None
  a = a_matrix.values
  b = b_matrix.values
  aux = []
  ja = 0
  jb = 0
  while ja < a_matrix.number_of_elements and jb < b_matrix.number_of_elements:
    while ja < a_matrix.number_of_elements and jb < b_matrix.number_of_elements and \
        compare((a[ja][0], a[ja][1]), (b[jb][0], b[jb][1])) == 1:
      aux.append(a[ja])
      ja += 1
    while ja < a_matrix.number_of_elements and jb < b_matrix.number_of_elements and \
        compare((a[ja][0], a[ja][1]), (b[jb][0], b[jb][1])) == 2:
      aux.append(b[jb])
      jb += 1
    while ja < a_matrix.number_of_elements and jb < b_matrix.number_of_elements and \
        compare((a[ja][0], a[ja][1]), (b[jb][0], b[jb][1])) == 0:
      aux.append((a[ja][0], a[ja][1], a[ja][2] + b[jb][2]))
      ja += 1
      jb += 1
  while ja < a_matrix.number_of_elements:
    aux.append(a[ja])
    ja += 1
  while jb < b_matrix.number_of_elements:
    aux.append(b[jb])
    jb += 1
  return SparseMatrix(a_matrix.number_of_lines, aux, [0] * a_matrix.number_of_lines, 1)


def multiply_sparse_matrix_with_a_vector(a):
  if not a.is_sparse_matrix:
    return None
  number_of_lines = a.number_of_lines
  a = a.values
  rez = []
  ind = 0
  for i in range(number_of_lines):
    element = 0
    while ind < len(a) and a[ind][0] == i:
        element += (number_of_lines - a[ind][1]) * a[ind][2]
        ind += 1
    rez.append(element)
  return rez


def find_start_line(current_index, row, matrix_elements):
  for i in range(current_index, min(current_index + 10, len(matrix_elements)) + 1):
    if matrix_elements[i][0] == row and matrix_elements[i][1] == -row:
      return i
  return -100


def sparse_matrix_multiplication(a, b):
  if not a.is_sparse_matrix or not b.is_sparse_matrix:
    return None
  lines = a.number_of_lines
  a = a.values
  b = b.get_order_after_columns()

  current_line_start = 0
  product = []
  for row in range(lines):
    if row % 100 == 0:
      print(row)
    jb = 0
    product.append((row, -row, 0))
    current_line_start = find_start_line(current_line_start, row, a)
    for column in range(lines):
      element = 0
      ja = current_line_start
      while ja < len(a) and jb < len(b) and a[ja][0] == row and b[jb][1] == column:
        while ja < len(a) and jb < len(b) and a[ja][0] == row and b[jb][1] == column and a[ja][1] < b[jb][0]:
          ja += 1
        while ja < len(a) and jb < len(b) and a[ja][0] == row and b[jb][1] == column and a[ja][1] > b[jb][0]:
          jb += 1
        while ja < len(a) and jb < len(b) and a[ja][0] == row and b[jb][1] == column and a[ja][1] == b[jb][0]:
          element += a[ja][2] * b[jb][2]
          ja += 1
          jb += 1
      while jb < len(b) and b[jb][1] == column:
        jb += 1
      if element > 0:
        product.append((row, column, element))
  product.append((lines, -lines, 0))
  if product[1][0] == 0 and product[1][1] == 0:
    del product[0]
  return SparseMatrix(lines, product, [0] * lines, 1)


def equal_matrixes(a, b):
  a = a.values
  b = b.values
  eps = 0.00000001
  if len(a) != len(b):
    return False
  for i in range(len(a)):
    if a[i][0] == b[i][0] and a[i][1] == b[i][0] and abs(a[i][2] - b[i][2]) > eps:
      print(i)
      return False
  return True


def equal_vectors(a, a_matrix):
  for i in range(a_matrix.number_of_lines):
    if a[i] != a_matrix.check_value[i]:
      return False
  return True
