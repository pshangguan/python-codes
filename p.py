def solution(P):

    for n in xrange(2,P+1):
        for k in xrange(2,n):
            if n % k == 0:
                break
        else:
            print("%d is a prime number!" % n)

solution(177)

