def merge_sort(A):
    merge_sort2(A,0,len(A)-1)

def merge_sort2(A,first,last):
    if first < last:
        mid = (first + last)//2
        merge_sort2(A,first,mid)
        merge_sort2(A,mid+1,last)
        merge(A,first,mid,last)

def merge(A,first,mid,last):
    L = A[first:mid]
    R = A[mid:last+1]
    L.append(99999999)
    R.append(99999999)
    i = j = 0
    for k in range(first, last+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j] 
            j += 1

A=[21,3,9,7,11,10,2,17]
merge_sort(A)

print(A)
