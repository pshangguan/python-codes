import math

A=[6,5,3,8,7,-1,14,2,-7,10]
B=[]

print(A)

def sortlist(a):
    print a
    if len(B) == 0:
       B.append(a)
    else:
       for j in range(len(B)):
           if a < B[j]:
                B.insert(j,a) 
                break
       if a >= B[len(B)-1]:
                B.append(a)

for i in range(len(A)):
   sortlist(A[i])

print(B) 
