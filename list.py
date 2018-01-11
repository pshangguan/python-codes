#!/usr/bin/python
import os,sys

longlist = []
fh=open("1.txt","r")

for f in fh:
	print(f)
	f = f.split()
	longlist += [word for word in f if word != "the"]
fh.close()

print(longlist)

