def bubble_sort(A):
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-1-i):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1], A[j]
    return A

A=[12,4,7,2,21,13,9,1]
print(bubble_sort(A))
