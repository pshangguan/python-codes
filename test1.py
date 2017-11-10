
def search(A):
    stack={}
    for i in range(len(A)):
        stack[A[i]] = 0

    for i in range(len(A)):
        stack[A[i]] += 1

    mid = (len(A)) //2

    a=stack.keys()
    for k in a:
        print(k)

    b=stack.values()
    for item in range(len(b)):
        if b[item] > mid:
            return 1
            break
    return -1

A=[3,1,4,6,1,1,1,10,1,1]
print(search(A))

L= [-1] + A

print(L)
