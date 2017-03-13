'''
find the pair of numbers whose difference is equal to the target

Runtime : O(N)
Memory : constant

Example: 
numbers  = [3,4,5,6,7,8,9,10,11]
target = 6
output= (5,11),(4,10),(3,9)
'''

def find_pair(numbers, target):
   
    i = 0
    j = len(numbers)-1

    while (i<j and i>=0 and j<= len(numbers)-1):
        if numbers[j]-numbers[i]> target:
            i+=1
        elif numbers[j] - numbers[i] < target:
            i-=1
        
        elif numbers[j] - numbers[i] == target:
            print numbers[i], numbers[j]
            i +=1
            j -=1





numbers  = [3,4,5,6,7,8,9,10,11]
target = 6


find_pair(numbers, target)
