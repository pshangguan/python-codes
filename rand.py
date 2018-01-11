#!/usr/bin/python

import random
# from shutil import copyfile
import shutil
import time

def genrand(n):
	s = {}
	for i in xrange(n):
		s[i] = random.randint(1,101)
	return s

r = genrand(10)
print r
for key in r:
	print(key,r[key])

shutil.copy("1.txt","/Users/guest1/scripts/new_1.txt")

shutil.copytree("../python","/Users/guest1/python2")
shutil.rmtree("/Users/guest1/python2")

time.sleep(1)

print("Wake up!")
