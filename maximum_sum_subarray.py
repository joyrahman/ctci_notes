'''
maximum sum subarry

'''


import sys


def max_subarray_sum(a):
  max_so_far = - sys.maxint - 1
  max_ending_here = 0

  for i in xrange(0,len(a)):
    max_ending_here = max_ending_here + a[i]
    if max_so_far < max_ending_here:
      max_so_far = max_ending_here

    if max_ending_here <0:
      max_ending_here = 0
  return max_so_far


a  = [2,4,7,10,-1,5,3,-9,2,20,30,5,4]

print max_subarray_sum(a)
