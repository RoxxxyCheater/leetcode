# 2319. Check if Matrix Is X-Matrix
# Easy

# A square matrix is said to be an X-Matrix if both of the following conditions hold:

#     All the elements in the diagonals of the matrix are non-zero.
#     All other elements are 0.

# Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.

 

# Example 1:

# Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
# Output: true
# Explanation: Refer to the diagram above. 
# An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
# Thus, grid is an X-Matrix.

# Example 2:

# Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
# Output: false
# Explanation: Refer to the diagram above.
# An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
# Thus, grid is not an X-Matrix.

 

# Constraints:

#     n == grid.length == grid[i].length
#     3 <= n <= 100
#     0 <= grid[i][j] <= 105

# Accepted
# 48,928
# Submissions
# 74,888


class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        
        # Проверка условия 1: все элементы на диагоналях матрицы ненулевые
        for i in range(n):
            if grid[i][i] == 0:  # Проверка главной диагонали
                return False
            if grid[i][n - 1 - i] == 0:  # Проверка побочной диагонали
                return False
        
        # Проверка условия 2: все остальные элементы матрицы равны 0
        for i in range(n):
            for j in range(n):
                if i != j and j != n - 1 - i and grid[i][j] != 0:  # Проверка наличия ненулевых элементов, кроме диагональных
                    return False
        
        return True  # Если оба условия выполняются, матрица является X-матрицей
     
lg = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]], [[5,7,0],[0,3,1],[0,5,0]]

for g in lg:
   Solution.checkMatrix('Success', g)
