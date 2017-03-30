

class Heap:
    def __init__(self,arr):
        self.arr = arr
        self.capacity = len(arr)
        self.current_size = len(arr)
        self.build_min_heap()

    def heapify(self,i):
        smallest = i
        l = 2*i + 1
        r = 2*i + 2

        if (l<self.current_size and self.arr[l] < self.arr[smallest]):
            smallest = l 

        if (r < self.current_size  and self.arr[r] < self.arr[smallest]):
            smallest  = r

        if smallest != i: 
            self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
            self.heapify(smallest)

    def build_min_heap(self):
        n = self.capacity
        for i in xrange(n-1,0,-1):
            self.heapify(i)

    def extract_min(self):
        temp = None
        if self.current_size>0:
            temp = self.arr[0]
            self.arr[0] = self.arr[self.current_size-1]
            self.current_size -= 1
            self.heapify(0)
        return temp

    def print_heap(self):
        for i in xrange(self.capacity):
            print self.arr[i],


def main():
    test   = [1,2,3,4,5,6,6,1,3,4,6]
    print test
    h = Heap(test)
    h.print_heap
    for i in xrange(len(test)):
        print "min",i, ">>",h.extract_min()

if __name__ == "__main__":
    main()
