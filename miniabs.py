import sys

def solution(A,N):
    min = sys.maxsize
    print(min)
    for i in xrange(0,N):
        for j in xrange(i,N):
            tmp = 0
            if i == j:
                tmp = A[i]
            else:
                for k in range(i,j):
                    tmp += A[k]
            print("real %d" % tmp)
            print("abs %d" % abs(tmp))
            if min > abs(tmp):
                min = abs(tmp)
            print(i,j,A[i],A[j],abs(tmp))

    return min

A=[2,-4,6,-3,9]
print("Result = %d" % solution(A,len(A)))

