def solution(A,B):
    result=0
    for i in range(len(A)):
        A[i] = A[i] + (float(B[i])/1000000)
    print(A)

    for i in range(len(A)):
        for j in range(i+1,len(A)):
            t1 = A[i] * A[j]
            t2 = A[i] + A[j]
            if (A[i] * A[j] >= A[i] + A[j]):
                result += 1
                print(i,j)
    return result

A=[0,1,2,2,3,5]
B=[500000,500000,0,0,0,20000]

print(solution(A,B))

