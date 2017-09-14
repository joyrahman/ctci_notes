
def find_kth_largest(array, pos):
    if pos < 0 or pos > len(array):
        return 0
    # try to find the item
    # logical position will be pos-1, indexed from 0
    # start 0 
    # end : len(array) - 1
    p = find( array, pos-1, 0, len(array))
    return array[p]


def find(array, k, start, end):
    pivot = partition(array, start, end)
    if pivot == k:
        return pivot
    # case2: go to left partition
    elif pivot > k:
        pivot = find(array, k, start, pivot)
    # case3: go to the right partition
    else:
        pivot = find(array, k, pivot + 1 , end) 

    return pivot 





def partition(array, start, end):
    r = start
    i = start
    for j in xrange(start+1, end):
        if array[j] > array[r]:
            i += 1 
            exchange(array, i, j )

    # now final exchange
    exchange(array, r, i ) 
    return i 


def exchange( array, i, j ) : 
    array[i], array[j] = array[j], array[i]
          


def main():
    test  = [10,105,13,43,56,2,7,8,15,25]
    k = int(raw_input("k:"))
    print test
    print find_kth_largest(test,k)
    print sorted(test)


if __name__ == "__main__":
    main()


