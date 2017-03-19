#!/usr/bin/python

m = 0
s = 0

# precizia masina
while True:
	s = 1.0 + pow(10, -m)
	#print '%.25f %f' % (s, m)
	if s == 1.0:
		break
	m += 1
m -= 1
print "Valoarea lui m a preciziei masina:"
print m

# neasociativitatea
x = 1.0
y = pow(10, -m)
z = pow(10, -m)
# verificare adunare
print "\n\nVerificarea neasociativitatii adunarii:"
print ((x + y) + z == x + (y + z))

# cautare pt inmultire
x = 10.0
m = 0
while m < 10000:
	y,z = pow(10, -m), pow(10, -m)
	if (x*y)*z != x*(y*z):
		print "\n\n\nNeasociativitatea inmultirii:"
		print '%.25f %.25f' % ((x*y)*z, x*(y*z))
		break
	m += 1

