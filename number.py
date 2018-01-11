import os, sys, re

def lookfornumber():

	f = open("1.txt","r")

	for x in f:
		match = re.search('\d.*',x)
		if match:
			print(x.strip())

print("I will find all the numbers in this file...")
lookfornumber()

