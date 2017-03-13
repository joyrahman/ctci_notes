

def count_sort(A):

    # assume the range is 10
    num_range  = 10
    C = [0 for _ in xrange(num_range)]

    for i in xrange(len(A)):
        C[A[i]]= C[A[i]] + 1
    
    # do the cumalative

    for i in xrange(num_range):
        C[i] = C[i-1] + C[i]

    B = [0 for _ in xrange(len(A))]

    for i in xrange(len(A)):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1
        
