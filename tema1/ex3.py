#!/usr/bin/python

from math import factorial, pi, sin
from time import time 

import random
import math

from Tkinter import *


c = [1.0/factorial(x) for x in range(3,14,2)]
times_simplified = [0] * 6
times_unsimplified = [0] * 6
hierarchy = [0] * 6

def times(x):
	global c
	global times_simplified, times_unsimplified

	v = [0] * 6
	y = x*x
	# P1
	# simplified 
	start = time()
	x*(1 + y*(-c[0] + c[1]*y))
	end = time()
	times_simplified[0] = times_simplified[0] + (end - start)
	# unsimplified
	start = time()
	x - c[0]*math.pow(x,3) + c[1]*math.pow(x,5)
	end = time()
	times_unsimplified[0] = times_unsimplified[0] + (end - start)
	
	# P2
	# simplified
	start = time()
	x*(1 + y*(-c[0] + y*(c[1] - c[2]*y)))
	end = time()
	times_simplified[1] = times_simplified[1] + (end - start)
	# unsimplified
	start = time()
	x - c[0]*math.pow(x,3) + c[1]*math.pow(x,5) - c[2]*math.pow(x,7)
	end = time()
	times_unsimplified[1] = times_unsimplified[1] + (end - start)

	# P3
	# simplified
	start = time()
	x*(1 + y*(-c[0] + y*(c[1] + y*(-c[2] + c[3]*y))))
	end = time()
	times_simplified[2] = times_simplified[2] + (end - start)
	# unsimplified
	start = time()
	x - c[0]*math.pow(x,3) + c[1]*math.pow(x,5) - c[2]*math.pow(x,7) + c[3]*math.pow(x,9)
	end = time()
	times_unsimplified[2] = times_unsimplified[2] + (end - start)

	# P4
	# simplified
	start = time()
	x*(1 + y*(-0.166 + y*(0.00833 + y*(-c[2] + c[3]*y))))
	end = time()
	times_simplified[3] = times_simplified[3] + (end - start)
	# unsimplified
	start = time()
	x - 0.166*math.pow(x,3) + 0.0083*math.pow(x,5) - c[2]*math.pow(x,7) + c[3]*math.pow(x,9)
	end = time()
	times_unsimplified[3] = times_unsimplified[3] + (end - start)
	
	# P5
	# simplified
	start = time()
	x*(1 + y*(-c[0] + y*(c[1] + y*(-c[2] + y*(c[3] - c[4]*y)))))
	end = time()
	times_simplified[4] = times_simplified[4] + (end - start)
	# unsimplified
	start = time()
	x - c[0]*math.pow(x,3) + c[1]*math.pow(x,5) - c[2]*math.pow(x,7) + c[3]*math.pow(x,9) - c[4]*math.pow(x,11)
	end = time()
	times_unsimplified[4] = times_unsimplified[4] + (end - start)

	# P6
	# simplified
	start = time()
	x*(1 + y*(-c[0] + y*(c[1] + y*(-c[2] + y*(c[3] + y*(-c[4] + c[5]*y))))))
	end = time()
	times_simplified[5] = times_simplified[5] + (end - start)
	# unsimplified
	start = time()
	x - c[0]*math.pow(x,3) + c[1]*math.pow(x,5) - c[2]*math.pow(x,7) + c[3]*math.pow(x,9) - c[4]*math.pow(x,11) + c[5]*math.pow(x,13)
	end = time()
	times_unsimplified[5] = times_unsimplified[5] + (end - start)


def approximations(x):
	global c
	v = [0]*6
	v[0] = x - c[0]*math.pow(x,3) + c[1]*math.pow(x,5)
	v[1] = v[0] - c[2]*math.pow(x,7)
	v[2] = v[1] + c[3]*math.pow(x,9)
	v[3] = x - 0.166*math.pow(x,3) + 0.0083*math.pow(x,5) - c[2]*math.pow(x,7) + c[3]*math.pow(x,9)
	v[4] = v[2] - c[4]*math.pow(x,11)
	v[5] = v[4] + c[5]*math.pow(x,13)
	return v

def best(x, app):
	s = sin(x)
	err = [math.fabs(s-app[i]) for i in range(len(app))]
	return err

def main():
	global hierarchy
	best_app = [0]*6
	for i in range(10000):
		x = random.uniform(-pi/2.0, pi/2.0)
		v = approximations(x)
		b = best(x,v)
		best_app = [x + y for x,y in zip(best_app, b)]
	hierarchy = [(i, best_app[i]) for i in range(len(best_app))]
	hierarchy = sorted(hierarchy, key = lambda x: x[1])
	for i in range(100000):
		x = random.uniform(-pi/2.0, pi/2.0)
		times(x)
	# print times_unsimplified
	# print times_simplified
	# return hierarchy
	

'''
Tabel grafic
'''
class SimpleTable(Frame):
	def __init__(self, parent, t1=[], t2=[]):
		Frame.__init__(self, parent, background="black")
		self._widgets = []
		for row in range(len(t1)+1):
			current_row = []
			# for column in range(columns):
			# 	label = Label(self, text="%s/%s" % (row, column), 
			# 					 borderwidth=0, width=10)
			# 	label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
			# 	current_row.append(label)
			if row == 0:
				label0 = Label(self, text="Times", borderwidth=0, width=10)
				label0.grid(row=row,column=1,sticky="nsew", padx=1, pady=1)
				current_row.append(label0)

				label1 = Label(self, text="Unsimplified", borderwidth=0, width=10)
				label1.grid(row=row,column=2,sticky="nsew", padx=1, pady=1)
				current_row.append(label1)

				label2 = Label(self, text="Simplified", borderwidth=0, width=10)
				label2.grid(row=row,column=3,sticky="nsew", padx=1, pady=1)
				current_row.append(label2)
			else:
				label1 = Label(self, text="Polynom %d" % (row), borderwidth=0, width=10)
				label1.grid(row=row,column=1,sticky="nsew", padx=1, pady=1)
				current_row.append(label1)
				
				label2 = Label(self, text="%.5f" % t1[row-1], borderwidth=0, width=10)
				label2.grid(row=row,column=2,sticky="nsew", padx=1, pady=1)
				current_row.append(label2)
				
				label3 = Label(self, text="%.5f" % t2[row-1], borderwidth=0, width=10)
				label3.grid(row=row,column=3,sticky="nsew", padx=1, pady=1)
				current_row.append(label2)
			self._widgets.append(current_row)

		for column in range(3):
			self.grid_columnconfigure(column, weight=1)
			
	def set(self, row, column, value):
		widget = self._widgets[row][column]
		widget.configure(text=value)



main()	
print (hierarchy)
root = Tk()

root.title("Tema 1 - Calcul Numeric")

app = Frame(root, width=500, height=500)
app.grid(row=0,column=0,sticky="NW")
app.grid_propagate(0)
app.update()

background_image = PhotoImage(file="ss-ConvertImage.gif")
background_label = Label(app, image=background_image)
background_label.photo=background_image
background_label.place(x=0, y=0)

title_label = Label(app, text="Approximating sine function", font=("Helvetica", 24))
title_label.place(x=250, y=40, anchor="center")


table_frame = Frame(app)
t = SimpleTable(table_frame, times_unsimplified,times_simplified)
t.grid(row=2,column=1)
table_frame.place(x=250, y=200, anchor="center")

hierarchy_frame = Frame(app)
for i in range(6):
	label = Label(hierarchy_frame, text="Best polynom is %d with %d approximations" %(hierarchy[i][0] + 1, hierarchy[i][1]))
	label.grid()
hierarchy_frame.place(x=100, y=300)

root.mainloop()



