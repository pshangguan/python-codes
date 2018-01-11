import os,sys,pwd

pwdall = pwd.getpwall()

for p in pwdall:
	print(p[0],p[1],p[6])

