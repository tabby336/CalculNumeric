#!/usr/bin/python
import math
import numpy

from methods import methods

n = None
m = None
eps = None
kmax = None
matrix = []

#done
def read_data():
	global n, m, eps, matrix, kmax
	fd = open("date.in", "r")
	n,m = fd.readline().split()
	n = int(n)
	m = int(m)
	eps = int(fd.readline())
	eps = math.pow(10, -eps)
	kmax = int(fd.readline())

	for i in range(n):
		line = fd.readline()
		line = [float(num) for num in line.split() ]
		matrix.append(line)

#done
def column(matrix, i):
    return [row[i] for row in matrix]

#done
def suma_modul(nums):
	s = 0
	for n in nums:
		s += math.fabs(n)
	return s

#done
def a_1(matrix):
	# suma maxima a modulelor de pe coloana
	s = suma_modul(column(matrix,0))
	for i in range(len(matrix[0])):
		_s = suma_modul(column(matrix,i))
		if _s > s:
			s = _s
	return s

#done
def a_inf(matrix):
	# suma maxima a modulelor de pe linie
	s = suma_modul(matrix[0])
	for row in matrix:
		_s = suma_modul(row)
		if _s > s: 
			s = _s
	return s

#done
def get_v0(matrix, method): 
	# folosind formulele 5 si 6
	if method == "schultz":
		ainf = a_inf(matrix)
		a1 = a_1(matrix)
		a = ainf * a1
		#return [[matrix[j][i]/a for i in range(len(matrix))] for j in range(len(matrix))]
		v0 = [[matrix[i][j]/a for i in range(len(matrix))] for j in range(len(matrix[0]))]
		return v0

	else:
		# this needs to be replaced i think; not correct
		ainf = a_inf(matrix)
		a1 = a_1(matrix)
		a = ainf * a1
		v0 = [[matrix[i][j]/a for i in range(len(matrix))] for j in range(len(matrix[0]))]
		return v0

#done	
def delta_v(v1, v0):
	# norma diferentei
	s = 0
	for i in range(len(v1)):
		for j in range(len(v1[0])):
			s += math.fabs(v1[i][j] - v0[i][j])
	return s

def get_norm(matrix, inv):
	s = 0
	c = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			for k in range(len(matrix[0])):
				c[i][j] = c[i][j] + matrix[i][k]*inv[k][j]

	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if i == j:
				s += math.fabs(c[i][j] - 1)
			else:
				s += math.fabs(c[i][j])
	return s



def calculate_inverse(matrix, method):
	global kmax
	global eps

	b = [[-matrix[j][i] for i in range(len(matrix))] for j in range(len(matrix))]

	delta = None
	v0 = get_v0(matrix, method)
	v1 = get_v0(matrix, method)
	
	for k in range(kmax):
		v0 = v1[:]
		v1 = methods[method](matrix, b, v0)
		delta = delta_v(v1,v0)

		if delta < eps or delta > math.pow(10, 10):
			break

	if delta < eps: #gasit app
		norm = get_norm(matrix, v1)
		return (v1,norm, k)
	else:
		return ("divergent",k)

def get_matrix(n):
	matrix = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		matrix[i][i] = 1
		try: 
			matrix[i][i+1] = 2
		except:
			pass

	return matrix

if __name__ == '__main__':
	read_data()
	# for row in matrix:
	# 	print row
	v0 = get_v0(matrix, "schultz")
	inv = calculate_inverse(matrix, "schultz")
	print inv[1]
	print inv[2]
	# global kmax, eps
	# kmax = 100
	# eps = math.pow(10, -15)
	# for i in range(2,10):
	# 	matrix = get_matrix(i)
	# 	for row in matrix: print row
	# 	print "\n\n"
	# 	r =  calculate_inverse(matrix, "schultz")
	# 	for row in r[0]: print row
	# 	print "Norm %d" % r[1]
	# 	print "Iters %d" % r[2]

	# 	print "\n\n\n"
	
	# 