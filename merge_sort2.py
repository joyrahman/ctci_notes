

def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]

        merge_sort(left)
        merge_sort(right)


        index = 0
        i = 0
        j = 0

        while (i <len(left) and j< len(right)):
            if left[i] < right[j]:
                alist[index] = left[i]
                i +=1
            else:
                alist[index] = right[j]
                j +=1
            index += 1 
        while i < len(left):
            alist[index] = left[i]
            i +=1
            index +=1

        while j < len (right):
            alist[index] = right[j]
            j += 1
            index += 1


alist = [10,9,5,6,7,3,2,11,6,19,20]
merge_sort(alist)
print alist



