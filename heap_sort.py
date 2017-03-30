
# n => number of elements
# i => root at i
def heapify(arr,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    # check left and root
    if l<n and arr[i] < arr[l]:
        largest = l
    # check largest and right
    if r < n and arr[largest] < arr[r]:
        largest = r
    #change root if needed
    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        print ("d2:",i,")",arr)
        # heapfiy the root with the changes for max heapify
        heapify(arr, n, largest)



# heap sort an array of given size


def heapSort(arr):
    n = len(arr)
    # build maxheap
    for i in range(n, -1, -1):
        heapify (arr, n, i)
        print "d1",arr
    # one by one extract elements
    for i in range(n-1,0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)



arr = [2,1,19,12,11,13,5,6,7]
heapSort(arr)
n = len(arr)
print arr
