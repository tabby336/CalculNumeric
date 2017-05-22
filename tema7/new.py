#!/usr/bin/python
import math
import random

def calculate_polynomial_value(f, x):
    fx = 0
    for index in range(len(f)):
        fx += f[index] * math.pow(x,index)
    return fx

def calculate_function_values(lower, upper, coeffs, num=10):
    function_values = [(lower, calculate_polynomial_value(coeffs, lower)),(upper, calculate_polynomial_value(coeffs, upper))] # empty the values from last request
    _values = [lower,upper]
    while len(function_values) != num:
        x = random.uniform(lower, upper)
        if x not in _values:
            function_values.append((x, calculate_polynomial_value(coeffs, x)))
            _values.append(x)

    function_values.sort(key = lambda k: k[0])
    return function_values

def calculate_divided_difference(before, pas, f):
    now = []
    for pair in range(0, len(f)-pas):
        if pas == 1:
            used = f[pair:pair+pas+1]
            now.append( (used[1][1] - used[0][1])/(used[1][0] - used[0][0]) )
        else:
            now.append( (before[pair+1] - before[pair])/(f[pair+pas][0] - f[0][0]) )
    return now

def approximate_lagrange(y,f,value):
    fx = y[0];
    for index in range(1,len(y)):
        p = 1
        for j in range(index):
            p = p*(value - f[j][0])
        fx = fx + p*y[index]
    return fx



if __name__ == '__main__':
    lower = 1
    upper = 5
    coeffs = [12, 0, 30, -12, 4]
    n = 100
    
    function_values = calculate_function_values(lower, upper, coeffs, n)
    y = [function_values[0][1]]
    now = []
    for pas in range(1,n):
        now = calculate_divided_difference(now, pas, function_values)
        y.append(now[0])
    
    a = approximate_lagrange(y,function_values, 3)
    b = calculate_polynomial_value(coeffs, 3)
    print a
    print b



