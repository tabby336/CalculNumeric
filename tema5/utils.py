def matrix_as_string(matrix):
    s = ""
    for row in matrix:
        s += ' '.join(str('%.15f' % e).rstrip('0').rstrip('.') for e in row)
        s += ' '
    return s