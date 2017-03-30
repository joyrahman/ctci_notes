def split_array(arr):
    index = 0
    total = arr[index]
    my_sum = [ 0 for x in xrange(len(arr))]
    arr_total = sum(arr[0:len(arr)])
    for i in xrange(len(arr)):
        arr_total = arr_total - arr[i]
        my_sum[i] = arr_total

    while(index < len(arr)):
        if total < my_sum[index]:
            index +=1
            total += arr[index]
        if total == my_sum[index]:
            return arr[:index+1],arr[index+1:]
        if total > my_sum[index]:
            return False
# optimization : how can you minimize computation of sum?



arr=[[1,2,3,3,2,1],[1,2,3,4,5,6,21],[1,90, 50, 30, 5, 3, 2, 1 ],[1, 50, 900, 1000 ]]

for test in arr:
    print test, ">>"
    print split_array(test)

