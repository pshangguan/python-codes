from array import *

def pick_num(A):

    for i in range(len(A)):
        tot1=0
        for j in range(0,i+1):
            tot1 += A[j] 

        tot2=0
        for k in range(i+2,len(A)):
            tot2 += A[k]

        if tot1 == tot2:
            print(i+1)

A=array("i",[-1,3,-4,5,1,-6,2,1])
pick_num(A)
