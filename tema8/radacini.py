import numpy as np
import cmath
import random

EPS = 0.01

def cmp(x, y):
	global EPS
	d = np.absolute(x) - np.absolute(y)
	# print(d)
	# raw_input("Paam")
	if (d < -EPS):
		return -1
	elif (d > EPS):
		return 1
	# print("Buna ziua")
	return 0

def cmp1(x, y):
	global EPS
	d = np.absolute(x) - np.absolute(y)
	print(d)
	# raw_input("Paam")
	if (d < -EPS):
		return -1
	elif (d > EPS):
		return 1
	# print("Buna ziua")
	return 0

def get_horner_reminder(p, x):
	return horner(p, x)[1]

def compute_diference(reminder, first, second, x, n):
	G = get_horner_reminder(first, x) / reminder
	H = G * G - get_horner_reminder(second, x) - reminder
	R = cmath.sqrt((n - 1) * (H * n - G * G))
	D1 = G + R
	D2 = G - R
	if (cmp(D1, D2) > 0):
		return n/D1
	return n/D2

def find_root(p, x):
	first = np.polyder(p)
	second = np.polyder(first)
	n = len(p)
	for i in range(10000):
		reminder = get_horner_reminder(p, x)
		if (cmp(reminder, 0) == 0):
			break;
		delta_x = compute_diference(reminder, first, second, x, n)
		x -= delta_x
		if (cmp (delta_x, 0) == 0):
			break;
	return x


def find_roots(poly):
	import random
	p = np.poly1d(poly)
	res = []
	q = p
	x = random.random()
	print(p)
	while (len(q) > 1 and x > 0):
		z = find_root(q, x)
		if (abs(np.imag(z)) < 0.01):
			# print(abs(np.imag(z)) < 0.00001)
			z = float(np.real(z))
		print(cmp1(horner(q, z)[1], 0))
		x = random.random()
		if (cmp1(horner(q, z)[1], 0) == 0):
			print("*********************")
			print(z)
			print(horner(q, z))
			res.append(z)
			q = horner(q, z)[0]
	res.append(q[0]*(-1)/q[1])
	return res

def horner(p, rad):
	rez = [p[len(p)]]
	for i in range(len(p)-1, 0, -1):
		rez.append(rez[-1] * rad + p[i])
	return (np.poly1d(rez), rez[-1] * rad + p[0])



poly = [1, 1, 1, 1, 1, 1]
p = np.poly1d(poly)
import random
print(find_roots(p))

