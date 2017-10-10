'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no
island, the maximum area is 0.)

Example 1:
           [[0,0,1,0,0,0,0,1,0,0,0,0,0],
           [0,0,0,0,0,0,0,1,1,1,0,0,0],
           [0,1,1,0,1,0,0,0,0,0,0,0,0],
           [0,1,0,0,1,1,0,0,1,0,1,0,0],
           [0,1,0,0,1,1,0,0,1,1,1,0,0],
           [0,0,0,0,0,0,0,0,0,0,1,0,0],
           [0,0,0,0,0,0,0,1,1,1,0,0,0],
           [0,0,0,0,0,0,0,1,1,0,0,0,0]]
           Given the above grid, return 6. Note the answer is not 11, because
           the island must be connected 4-directionally.
           Example 2:
           [[0,0,0,0,0,0,0,0]]
           Given the above grid, return 0.
           Note: The length of each dimension in the given grid does not exceed
           50.
'''

class Solution(object):
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.seen = set()
        ans = 0
        for i in xrange(len(self.grid)):
            for j in xrange(len(self.grid[0])):
                ans = max(ans, self.area(i,j))
        return ans
                            
        
    def area(self,r,c):
        if (r<0 or r>=len(self.grid) ) or ( c <0 or c>=len(self.grid[0])) or (r,c) in self.seen or self.grid[r][c]==0:
            return 0
        self.seen.add((r,c))
        return 1 + self.area(r-1,c) + self.area(r+1,c) + self.area(r,c-1) + self.area(r,c+1)
        




