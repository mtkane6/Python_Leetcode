'''
Runtime: 36 ms, faster than 79.40% of Python online submissions for Rotting Oranges.
Memory Usage: 11.7 MB, less than 75.00% of Python online submissions for Rotting Oranges.
-------------------------------------------------------------------------------------------------------

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rottenList = []
        counter = 0
        finished = False
        while not finished:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 2:
                        rottenList.append([i,j])

            changeMade = False
            while len(rottenList) != 0:
                a, b = rottenList.pop(0)
                #check above
                if a > 0:
                        if grid[a-1][b] == 1:
                            grid[a-1][b] = 2
                            changeMade = True
                            # continue
                #check below
                if a < len(grid)-1:
                    if grid[a+1][b] == 1:
                        grid[a+1][b] = 2
                        changeMade = True
                        # continue
                #check left
                if b > 0:
                    if grid[a][b-1] == 1:
                        grid[a][b-1] = 2
                        changeMade = True
                        # continue
                #check right
                if b < len(grid[0])-1:
                    if grid[a][b+1] == 1:
                        grid[a][b+1] = 2
                        changeMade = True
                        # continue
            if changeMade:
                counter += 1
                if any(grid):
                    for i in grid:
                        if 1 in i:
                            finished = False
                            break
                        else: finished = True

            else: finished = True



        if any(grid):
            for i in grid:
                if 1 in i:
                    return -1
        return counter