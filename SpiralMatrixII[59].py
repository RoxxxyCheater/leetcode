
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]


# Constraints:

# 1 <= n <= 20
# Accepted
# 486,849
# Submissions
# 701,201

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]  # Создаем матрицу размером n x n, заполненную нулями
        num = 1  # Начинаем с числа 1
        left, right, top, bottom = 0, n-1, 0, n-1  # Инициализируем границы матрицы

        while num <= n*n:
            # Обход вправо
            for col in range(left, right+1):
                matrix[top][col] = num
                num += 1
            top += 1

            # Обход вниз
            for row in range(top, bottom+1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # Обход влево
            for col in range(right, left-1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

            # Обход вверх
            for row in range(bottom, top-1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

        return matrix  # Возвращаем полученную матрицу

      
list_n = 3,1
for i in list_n:
  Solution.generateMatrix('Success', i)
