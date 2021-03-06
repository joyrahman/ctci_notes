
class Solution(object):
    def numDistinctIslands(self, grid):
        seen = set()

        def explore(r,c,r0,c0):
            if (0<=r < len(grid) and 0<=c <len(grid[0]) and grid[r][c] and (r,c) not in seen):
                seen.add((r,c))
                shape.add(( r - r0, c - c0))
                explore (r+1, c, r0, c0)
                explore (r-1, c, r0, c0)
                explore (r, c+1, r0, c0)
                explore (r, c-1, r0, c0)


        shapes = set()

        for r in xrange(len(grid)):
            for c in xrange(len(grid[0])):
                shape = set()
                explore(r,c,r,c)
                if shape:
                    print(shape)
                    shapes.add(frozenset(shape))
                    print ("shapes",shapes)
        return len(shapes)


def main():
    test = [[11000], [11000], [00011], [00011]]
    test2 = [[11011],[10000], [00001], [11011]]
    S = Solution()
    print S.numDistinctIslands(test)
    S2 = Solution()
    print S2.numDistinctIslands(test2)



if __name__ == "__main__":
    main()
