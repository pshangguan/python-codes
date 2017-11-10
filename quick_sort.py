def quick_sort(A):
    quick_sort2(A,0,len(A)-1)

def quick_sort2(A,first,last):
    if first < last:
        p=partition(A,first,last)
        quick_sort2(A,first,p-1)
        quick_sort2(A,p+1,last)

A=[12,21,22,33,6,45,9,7,18,51]
quick_sort(A)

