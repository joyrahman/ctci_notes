import heapq as heap

def k_largest(array,k):
    data = []
    
    # push the fist k elements
    for i in xrange(0,k):
        heap.heappush(data,array[i])
    # push pop next n-k elements
    
    for i in xrange (k, len(array)):
        t = heap.heappushpop(data, array[i])

    # print the remaining k elements in the heap
    result = []
    for i in xrange(k):
        result.insert(0,heap.heappop(data))
        #return [ heap.heappop(data) for i in range(k)]
    return result


def main():
    test = [12,5,787,1,23]
    k = 2
    print k_largest(test,k)
    


if __name__ == "__main__":
    main()
