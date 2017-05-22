import random 

def polinom(x):
	return x ** 4 - 12 * x ** 3 + 30 * x ** 2 + 12

def polinom2(x):
	return x ** 2

def polinom3(x):
	return x ** 2  + x + 1

def get_x(x0, xn, n, f):
	xs = [(x0, f(x0)), (xn, f(xn))]
	for i in range(1, n):
		x = random.uniform(x0, xn)
		xs.append((x, f(x)))
	xs.sort()
	return xs

def compute_Atiken(vals, n):
	# Atiken = [[0 for x in range(n)] for x in range(n)]
	# for i in range(0, n):
	# 	Atiken[0][i] = vals[i][1]

	# for i in range(1, n):
	# 	for j in range(i, n):
	# 		Atiken[i][j] = Atiken[i - 1][j] - Atiken[i - 1][j - 1]
	# Atiken_diag = [Atiken[i][i] for i in range(n)]
	# return Atiken_diag
	Atiken = [vals[i][1] for i in range(n + 1)]
	for k in range(1, n + 1):
		for i in range(n, k - 1, -1):
			Atiken[i] = (Atiken[i] - Atiken[i-1]) / (vals[i][0] - vals[i-k][0])
	return Atiken

def compute_value(x, x0, xn, n, func):
	xs = [(i, polinom(i)) for i in range(1, 6)]
	matr = compute_Atiken(xs, n)
	Lprec = xs[0][1]
	aux = 1
	for i in range(1, n + 1):
		aux *= (x - xs[i - 1][0])
		L = Lprec + aux * matr[i]
		Lprec = L
	return L

def values(x0, xn, n, func):
	x = x0
	display = {"expected": [], "real": [], "l_infinit": -100}
	while x < xn:
		x += 0.05
		computed = compute_value(x, 1, 5, 4, polinom)
		expected = polinom(x)
		display["expected"].append({"x": x, "y": expected})
		display["real"].append({"x": x, "y": computed})
		if (abs(computed - expected) > display["l_infinit"]):
			display["l_infinit"] = abs(computed - expected)
	return display

# print(worst_approximation(1, 5, 4, polinom))

# n = 4
# print(get_x(1, 7, n, polinom))
# x = compute_Atiken(get_x(1, 7, n, polinom), n)
# for y in x:
# 	print y

 