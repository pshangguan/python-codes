#!/usr/bin/python

import os,sys,re

def myself(n):
	if n == 0:
		return 1
	else:
		return n * myself(n-1)

x = input("Give me a positive integer: ")
print("%d! = %d" % (x,myself(x)))

