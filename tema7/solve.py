#!/usr/bin/python
import math

divided_differences = []
y = []
before = []
values = []

def calculate_polynomial_value(f, x):
	fx = 0
	for index in range(len(f)):
		fx += f[index] * math.pow(x,index)
	return fx

def solve(f):
	global y, values
	values = f[:]
	y = [f[0][1]]
	for index in range(1,len(f)):
		print "\n\n\nPasul %s" % str(index)
		calculate_divided_difference(index, f)
		print y		

def calculate_divided_difference(pas, f):
	global y,before

	now = []
	for pair in range(0, len(f)-pas):
		if pas == 1:
			used = f[pair:pair+pas+1]
			now.append( (used[1][1] - used[0][1])/(used[1][0] - used[0][0]) )
		else:
			now.append( (before[pair+1] - before[pair])/(f[pair+pas][0] - f[0][0]) )
	before = now[:]
	y.append(now[0])
	print "Y HERE"
	print y

def approximate_lagrange(x):
	global y, values
	print "Y HERE"
	print y

	#fx = calculate_polynomial_value(y, float(value))
	#fx = values[0][1]
	fx = values[0][1]
	print "paam"
	print values[0][1]
	for i in range(len(y)):
		p = 1
		for j in range(i):
			p *= (float(x) - values[j][0])
		fx = fx + p*y[i]
	print values

	return fx
