#!/usr/bin/python
import sys
import numpy
import scipy.linalg
import math
from functools import reduce 
import operator

def read_data():
	'''
	Citire date din fisier

	date.in contine in ordinea asta:
	n - dimensiunea matricei
	t - pentru precizia lui epsilon

	urmatoarele n linii: elementele matricei A
	ultima linie: termenii liberi (b)
	'''
	fd = open("date.in", 'r')

	n = int(fd.readline())
	t = int(fd.readline())
	epsilon = pow(10, -t)

	a = [[]]*n #matricea initiala

	for i in range(n):
		nums = fd.readline().split()
		nums = [float(num) for num in nums]	
		a[i] = nums

	b = fd.readline().split()
	b = [float(num) for num in b]
	return n, epsilon, a, b

n, epsilon, a, b = read_data()

def elem_diag_cholesky(p):
	global a, d
	s = 0
	for k in range(p):
		s = s + d[k]*a[p][k]*a[p][k]
	return  (a[p][p] - s)

def elem_matrix_cholesky(i,p):
	global epsilon, a, d
	s = 0
	for k in range(p):
		s += d[k]*a[i][k]*a[p][k]
	if abs(d[p]) > epsilon:
		return (a[i][p] - s)/d[p]
	else:
		sys.exit(0)


d = [0]*n #elem de pe diagonala d de dupa descompunere

def decomposition():
	global a,d
	for i in range(n):
		d[i] = elem_diag_cholesky(i)
		for j in range(i+1, n):
			# merge deasupra diagonalei principale si pune sub ea
			# ca sa parcurga cum trb
			a[j][i] = elem_matrix_cholesky(j,i)



init_a = a[:] # sa fie la LU
'''
Rezolvare Lz = b
 - elementele matricei L se considera a fi:
 	* 1 pe diag principala (considerate, nu efectiv stocate)
 	* sub diagonala principala ce-i in matricea a acum
 	* deasupra diag principale 0
'''
z = [0]*n
def direct_substition_term(i):
	global a, z, b
	s = 0
	for j in range(i):
		s += a[i][j]*z[j]
	return b[i] - s

def direct_substitution():
	global z
	for i in range(n):
		z[i] = direct_substition_term(i)


'''
Rezolvare Dy = z
'''
y = [0]*n
def diagonal_solve():
	global y, z
	for i in range(n):
		y[i] = z[i]/d[i]

'''
Rezolvare Lt x = y
'''
x = [0]*n
def back_substitution_term(i):
	global a,x,y
	s = 0
	for j in range(i+1, n):
		s += a[j][i]*x[j]
	return y[i] - s


def back_substitution():
	for i in range(n-1,-1,-1):
		x[i] = back_substitution_term(i)


'''
Descompunerea LU 
'''
P, L, U = scipy.linalg.lu(init_a)
lu = scipy.linalg.lu_factor(init_a)
lu_sol = scipy.linalg.lu_solve(lu, b)

'''
Treaba cu norma
'''
ax_terms = [0]*n

def norm_term(i):
	global n,a,x
	s = 0
	for j in range(n):
		if i > j:
			s += a[j][i] * x[j]
		else:
			s += a[i][j] * x[j]
	return s

def calculate_norm_terms():
	global a, b, x, ax_terms
	for i in range(n):
		ax_terms[i] = norm_term(i)

def calculate_norm():
	global ax_terms, b
	s = 0
	for i in range(n):
		s += (ax_terms[i] - b[i]) ** 2
	return math.sqrt(s)

def determinant():
	global d
	return (reduce(operator.mul, d, 1))

decomposition() #a
det = determinant() #det
direct_substitution() # z
diagonal_solve() #y
back_substitution() #x
# P L U
calculate_norm_terms() 
norm = calculate_norm() #norm

