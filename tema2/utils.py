def get_cholesky_matrices(n, a, d):
    l = [[0 for i in range(n)] for j in range(n)]
    lt = [[0 for i in range(n)] for j in range(n)]
    _d = get_determinant_matrix(n, d)

    _a = a[:]

    for i in range(n):
        l[i][i] = 1
        lt[i][i] = 1
        for j in range(i):
            l[i][j] = a[i][j]
            lt[j][i] = a[i][j]
            _a[i][j] = a[j][i]

    return _a, l, _d, lt

def get_determinant_matrix(n, d):
    return [[d[i] if i==j else 0 for i in range(n)] for j in range(n)]

def matrix_as_string(matrix):
    s = ""
    for row in matrix:
        s += ' '.join(str('%.15f' % e).rstrip('0').rstrip('.') for e in row)
        s += ' '
    return s

def vector_as_string(vector):
    return ' '.join(str('%.15f' % e).rstrip('0').rstrip('.') for e in vector)