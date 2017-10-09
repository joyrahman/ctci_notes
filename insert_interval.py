# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        merge_start = newInterval.start 
        merge_end = newInterval.end
        for item in intervals:
            if (item.end >= newInterval.start and item.start <=
                    newInterval.end):
                # the item is within boundary
                merge_start = min(merge_start,item.start)
                merge_end = max(merge_end, item.end)
            else:
                result.append(item)
        #create the final item and append to the result
        
        result.append(Interval(merge_start,merge_end))
        result = sorted(result,key=lambda x: x.start)
        return result
    

def main():
    intervals = []
    intervals.append(Interval(1,2))
    intervals.append(Interval(3,5))
    intervals.append(Interval(6,7))
    intervals.append(Interval(8,10))
    intervals.append(Interval(12,16))
    
    S = Solution()
    result = S.insert(intervals,Interval(4,9))
    for item in result:
        print item.start,item.end

if __name__ == "__main__":
    main()
