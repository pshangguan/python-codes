import sys

def solution(P):
    ## make sure to pick up the last number P
    for n in range(2, P+1):
        for x in range(2, n):
            if n % x == 0:
#                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
#            print(n, 'is a prime number')
             print n, 
solution(197)
