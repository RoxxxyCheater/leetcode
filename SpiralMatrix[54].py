# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# Accepted
# 1,070,059
# Submissions
# 2,319,695


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
                res = []
        if not matrix:
            return res
        
        rows, cols = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, cols-1, 0, rows-1
        
        while left <= right and top <= bottom:
            # traverse right
            for col in range(left, right+1):
                res.append(matrix[top][col])
            # traverse down
            for row in range(top+1, bottom+1):
                res.append(matrix[row][right])
            # traverse left
            if left < right and top < bottom:
                for col in range(right-1, left-1, -1):
                    res.append(matrix[bottom][col])
                # traverse up
                for row in range(bottom-1, top, -1):
                    res.append(matrix[row][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return res
    
    
list_matrix = [[1,2,3],[4,5,6],[7,8,9]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in list_matrix:
    Solution.spiralOrder('Success', i)
