def matrix_mul(a,b):
	n = len(a)
	m = len(a[0])
	c = [[0 for i in range(m)] for j in range(n)]
	for i in range(n):
		for j in range(m):
			for k in range(m):
				c[i][j] = c[i][j] + a[i][k]*b[k][j]
	return c

def schultz(a, minus_a, v):
	# Vk+1 = Vk*(2I - AVk)
	av = matrix_mul(minus_a, v)
	for i in range(len(av)):
		av[i][i] += 2
	v1 = matrix_mul(v, av)
	return v1

def formula2(a, minus_a, v):
	#Vk+1 = Vk(3I - AVk(3I - AVk))
	#Vk+1 = Vk(3I + (-A)Vk(3I + (-A)Vk))
	av = matrix_mul(minus_a, v)
	print av
	inner = [[av[i][j] for i in range(len(av))] for j in range(len(av))]
	for i in range(len(av)):
		inner[i][i] += 3
	avinner = matrix_mul(av,inner)
	outer =  [[avinner[i][j] for i in range(len(avinner))] for j in range(len(avinner))]
	for i in range(len(avinner)):
		outer[i][i] += 3
	return matrix_mul(v,outer)

def formula3(a, minus_a, v):
	#Vk+1 = (I + 0.25*(I - VkA)*(3I - VkA)^2)Vk
	va = matrix_mul(v,minus_a)
	x = [[va[i][j] for i in range(len(va))] for j in range(len(va))]
	for i in range(len(va)):
		x[i][i] += 3
	x = matrix_mul(x,x)

	y = [[va[i][j] for i in range(len(va))] for j in range(len(va))]
	for i in range(len(va)):
		y[i][i] += 1

	z = matrix_mul(y,x)
	for i in range(len(z)):
		for j in range(len(z)):
			if i == j:
				z[i][j] /= 0.25
				z[i][j] += 1
			else:
				z[i][j] /= 0.25

	return matrix_mul(z,v)


methods = {
	'schultz': schultz,
	'formula2': formula2,
	'formula3': formula3
}

