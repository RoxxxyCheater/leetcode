    
# Medium

# 5455

# 197

# Add to List

# Share
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
# Accepted
# 350,592
# Submissions
# 757,669
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  

        while queue:
            row, col, path_length = queue.popleft()

            if row == n - 1 and col == n - 1:  
                return path_length

            for drow, dcol in directions:
                new_row, new_col = row + drow, col + dcol

                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col, path_length + 1))
                    grid[new_row][new_col] = 1  

        return -1
    
inp_list = [[0,1],[1,0]],[[0,0,0],[1,1,0],[1,1,0]],[[1,0,0],[1,1,0],[1,1,0]]
for i in inp_list:
    Solution.shortestPathBinaryMatrix('Success', i)
