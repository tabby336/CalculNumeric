import random
import numpy as np
import math

EPS = 0.000000001

def der_first(x):
	poly_coef = [2, -4]
	p = np.poly1d(poly_coef)
	return np.polyval(p, x)

def der_second(x):
	return 2 * x + math.exp(x)

def der_third(x):
	poly_coef = [4, -18, 26, -12]
	p = np.poly1d(poly_coef)
	return np.polyval(p, x)

def der2_first(x):
	poly_coef = [2]
	p = np.poly1d(poly_coef)
	return np.polyval(p, x)

def der2_second(x):
	return 2 + math.exp(x)

def der2_third(x):
	poly_coef = [12, -36, 26]
	p = np.poly1d(poly_coef)
	return np.polyval(p, x)

def compute_delta(x, g):
	return ((x[1]-x[0]) * g(x[1])) / (g(x[1])-g(x[0]))

def get_minimum_point(der, der2):
	x = (random.random(), random.random())
	for i in range(10000):
		delta_x = compute_delta(x, der)
		if (abs(delta_x) < EPS):
			if (der2(x[1]) > 0):
				return x[1]
		elif (abs(delta_x) > 10**8):
			return None
		y = (x[1], x[1] - delta_x)
		x = y
	print(i)
	return None

print(get_minimum_point(der_first, der2_first))
print(get_minimum_point(der_second, der2_second))
print(get_minimum_point(der_third, der2_third))