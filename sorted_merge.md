# merge two sorted array, provided the first array has enough space to hold the second array

- runtime : O(len(a) + len(b))
  memory : O(len(a)) //no extra memory

```python

def sorted_marge(a,b,last_a,last_b):
    index_a = last_a - 1
    index_b = last_b - 1

    index = last_a + last_b -1 

    while (index_b >=0 and index_a >=0):
        print index_a, index_b
        if a[index_a] > b[index_b]:
            a[index] = a[index_a]
            index_a  -= 1
        else:
            a[index] = b[index_b]
            index_b -= 1

        index -= 1

    while index_b>=0:
        a[index] = b[index_b]
        index_b -= 1
        index -= 1


    return a






def main():
    a = [3,8,12,15,17,-1,-1,-1]
    b = [2,4,5]
    print sorted_marge(a,b,5,3)


if __name__ == "__main__":
    main()
```
