import random 
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

