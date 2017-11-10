import numpy
dir(numpy)

# import pandas as pd

mylist=[]
mylist.append(11)
mylist.append(12)
mylist.append(13)

t = 0
for i in mylist:
    t += i
    print (i)

print (t)

string="Hello World!"

print (string)

cnt=0
p=-1

while string.index("l",p+1) <= len(string):
    cnt += 1
    print ("at %d" % cnt)

    q=string.index("l",p+1) 
    print (q)
    p=q
    if cnt == string.count("l"):
        break

temperature = 115  
while temperature > 112: # first while loop code
    print(temperature)
    temperature = temperature - 1

first_array=[1,2,3]

if first_array:
    print ("hi")

def myfunc1():
    print ("In my first func!")

def myfunc2(name,sayit):
    print("My name is %s. %s" % (name,sayit))

def myfunc3(a,b):
    return a+b

myfunc1()

myfunc2("philip","hey yo!")

print(myfunc3(12,88))

