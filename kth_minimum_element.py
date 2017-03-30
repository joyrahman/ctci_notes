'''
partial quick sort
'''
import sys

def k_smallest(arr,l,r,k):
  if k>0 and k <= (r-l+1):
    pivot  = partition(arr,l,r)
    if (pivot-l == k-1):
      return arr[pivot]
    # more elements on left
    if (pivot-l > k-1 ):
      return k_smallest(arr, l, pivot-1, k)
    # else recur for right sub array
    return k_smallest(arr, pivot+1, r, k-pivot+l -1 )
  return sys.maxint

def partition(arr,l,r):
  pivot = arr[r]
  i = l

  for j in xrange(l,r):
    if arr[j] <= pivot:
      arr[i],arr[j] = arr[j], arr[i]
      i+=1
  #now swap the pivot and ith position
  arr[i],arr[r] = arr[r],arr[i]
  return i 


def main():
  test = [12,3,0,1,3,27,28,32,45,2,5,5,7,4,19,26]
  k = 5
  n = len(test)
  print test 
  print k_smallest(test, 0 , n-1, k)
  print test
  print test[k]


main()
