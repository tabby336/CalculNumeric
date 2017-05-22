import random 
import math
from numpy.polynomial.polynomial import polyval

def polinom(x, coef):
	return polyval(x, coef)

def get_x(x0, xn, n, coef):
	xs = [(x0, polinom(x0, coef)), (xn, polinom(xn, coef))]
	for i in range(1, n):
		x = random.uniform(x0, xn)
		xs.append((x, polinom(x, coef)))
	xs.sort()
	return xs

def compute_Atiken(vals, n):
	Atiken = [vals[i][1] for i in range(n + 1)]
	for k in range(1, n + 1):
		for i in range(n, k - 1, -1):
			Atiken[i] = (Atiken[i] - Atiken[i-1]) / (vals[i][0] - vals[i-k][0])
	return Atiken

def compute_value(x, x0, xn, n, coef):
	xs = get_x(x0, xn, n, coef)
	matr = compute_Atiken(xs, n)
	Lprec = xs[0][1]
	aux = 1
	for i in range(1, n + 1):
		aux *= (x - xs[i - 1][0])
		L = Lprec + aux * matr[i]
		Lprec = L
	return L

def values(x0, xn, n, coef):
	x = x0
	display = {"expected": [], "real": [], "l_infinit": -100}
	while x < xn:
		x += 0.05
		computed = compute_value(x, x0, xn, n, coef)
		expected = polinom(x, coef)
		display["expected"].append({"x": x, "y": expected})
		display["real"].append({"x": x, "y": computed})
		if (abs(computed - expected) > display["l_infinit"]):
			display["l_infinit"] = abs(computed - expected)
	return display

def fi(i, x):
	if (i % 2 == 0): 
		return math.cos(i / 2 * x)
	return math.sin((i + 1) / 2 * x)

def computed_fi_par(x, n, fi_matr):
	for i in range(n + 1):
		for j in range(0, n + 1, 2):
			fi_matr[i][j] = fi(j, x[i])
			# math.cos(j / 2 * x[i])

def computed_fi_impar(x, n, fi_matr):
	for i in range(n + 1):
		for j in range(1, n + 1, 2):
			fi_matr[i][j] = fi(j, x[i])
			# math.cos((j + 1)/ 2 * x[i])


def compute_fi(x, n):
	fi = [[0 for i in range(n + 1)] for i in range(n + 1)]
	computed_fi_par([val[0] for val in x], n, fi)
	computed_fi_impar([val[0] for val in x], n, fi)
	return fi

def get_periodic_function(x0, xn, n, f):
	xs = []
	for i in range(0, n + 1):
		x = random.uniform(x0, xn)
		xs.append((x, f(x)))
	xs.sort()
	return xs

def first_periodic(x):
	return math.sin(x) - math.cos(x)

def second_periodic(x):
	return math.sin(2*x) + math.sin(x) + math.cos(3*x)

def third_periodic(x):
	return math.sin(x) ** 2 - math.cos(x) ** 2

def compute_system(T, Y):
	import numpy
	a = numpy.array(T)
	b = numpy.array(Y)
	x = numpy.linalg.solve(a, b)
	return x

def solve_b(x_tilda, x0, xn, n, f):
	evaluare = None
	while (evaluare == None):
		try:
			x = get_periodic_function(x0, xn, n, f)
			T = compute_fi(x, n)
			sol = compute_system(T, [y[1] for y in x])
			evaluare = 0
			for i in range(n + 1):
				evaluare += sol[i] * fi(i, x_tilda)
		except:
			evaluare = None
	return evaluare


def grafic_b(x0, xn, n, f):
	display = {"expected": [], "real": [], "l_infinit": -100}
	x = x0
	while x < xn:
		x += 0.05
		computed = solve_b(x, x0, xn, n, f)
		expected = f(x)
		display["expected"].append({"x": x, "y": expected})
		display["real"].append({"x": x, "y": computed})
		if (abs(computed - expected) > display["l_infinit"]):
			display["l_infinit"] = abs(computed - expected)
	return display

# print(solve_b(math.pi / 7, 0, 31 * math.pi / 16, 20, second_periodic))

