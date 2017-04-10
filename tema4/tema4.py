class SparseMatrix:
  def __init__(self, number_of_lines, system_matrix, system_free_terms, type = 0):
    if type == 0:
      system_matrix = sorted(system_matrix, key=lambda x: x[0] * 1000000 + x[1])
      self.number_of_lines = number_of_lines
      self.system_matrix = []
      self.is_sparse_matrix = True
      j = 0
      for i in range(self.number_of_lines):
        if i != 0 or i == 0 and system_matrix[0][1] != 0:  #nu avem valoare diferita de 0 pe 0 0
          self.system_matrix.append((i, -i, 0))
        number_of_elements_on_current_line = 0
        while j < len(system_matrix) and system_matrix[j][0] == i:
          self.system_matrix.append(system_matrix[j])
          j += 1
          number_of_elements_on_current_line += 1
        if number_of_elements_on_current_line > 10:
          self.is_sparse_matrix = False
      self.system_matrix.append((number_of_lines, -number_of_lines, 0))
      self.number_of_elements = len(self.system_matrix)
      self.system_free_terms = system_free_terms
    else:
      self.number_of_lines = number_of_lines
      self.system_free_terms = system_free_terms
      self.system_matrix = system_matrix


def read_sparse_matrix(file_name):
  with open(file_name) as f:
    my_lines = f.readlines()
    my_lines = [line.strip() for line in my_lines if len(line.split()) > 0]
  number_of_elements = int(my_lines[0])
  system_free_terms = [float(x) for x in my_lines[1:number_of_elements + 1]]
  system_matrix = [tuple(x.split(", ")) for x in my_lines[number_of_elements + 1:]]
  system_matrix = [(int(x[1]), int(x[2]), float(x[0])) for x in system_matrix]
  return SparseMatrix(number_of_elements, system_matrix, system_free_terms)


def generate_dummy_solution(number_of_lines):
  return [0 for i in range(number_of_lines)]

def compute_values(solution, matrix):
  b = []
  nr = 0
  for i in range(matrix.number_of_lines):
    element = 0
    while nr < len(matrix.system_matrix) and matrix.system_matrix[nr][0] == i:
      if (matrix.system_matrix[nr][1] > 0 or (matrix.system_matrix[nr][1] == 0 and matrix.system_matrix[nr][2] != 0)):
        element += matrix.system_matrix[nr][2] * solution[matrix.system_matrix[nr][1]]
      nr += 1
    b.append(element)
  return b

def has_solution(matrix):
  cr = 0
  for i in range(matrix.number_of_lines):
    my_sum = 0
    x = 0
    while (matrix.system_matrix[cr][0] == i):
      if (matrix.system_matrix[cr][0] != matrix.system_matrix[cr][1]):
        my_sum += abs(matrix.system_matrix[cr][2])
      else:
        x =  abs(matrix.system_matrix[cr][2])
      cr +=1 
    if (x < my_sum): return False 
  return True


def find_solution(file_name):
  matrix = read_sparse_matrix(file_name)
  solution = generate_dummy_solution(matrix.number_of_lines)
  prec = generate_dummy_solution(matrix.number_of_lines)

  import time

  start = time.time()

  if (has_solution(matrix)):
    for k in range(10000):
      nr = 0
      for i in range(matrix.number_of_lines):
        solution[i] = matrix.system_free_terms[i]
        numitor = 0
        while nr < len(matrix.system_matrix) and matrix.system_matrix[nr][0] == i:
          if (matrix.system_matrix[nr][1] > 0 or (matrix.system_matrix[nr][1] == 0 and matrix.system_matrix[nr][2] != 0)):
            if matrix.system_matrix[nr][0] != matrix.system_matrix[nr][1]:
              solution[i] -= matrix.system_matrix[nr][2] * solution[matrix.system_matrix[nr][1]]
            else:
              numitor = matrix.system_matrix[nr][2]
          nr += 1
        solution[i] /= numitor
      error = max ([abs(solution[i] - prec[i]) for i in range(matrix.number_of_lines)])
      if error < 0.000000001:
        break
      prec = solution[:]
    values = compute_values(solution, matrix)
    error = max ([abs(values[i] - matrix.system_free_terms[i]) for i in range(matrix.number_of_lines)]) 
    result = {"error": error, 
              "nr_iteration": k, 
              "time": time.time() - start}
  else:
    result = {"nr_iteration": 9999, 
              "time": time.time() - start}

  print (solution)

  print (result)
  return result
  # print solution

# find_solution("m_rar_2017_1.txt")




