#!/usr/bin/python

import os,sys,re

def fib():
	a,b=1,1
	while True:
		yield a
		a,b=b,a+b

n = input("Enter a value:")

for i in fib():
	print("FIB = %d" % i)
	if i > n:
		break
