# 304. Range Sum Query 2D - Immutable
# Medium

# Given a 2D matrix matrix, handle multiple queries of the following type:

#     Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Implement the NumMatrix class:

#     NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
#     int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# You must design an algorithm where sumRegion works on O(1) time complexity.

 

# Example 1:

# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

 

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 200
#     -104 <= matrix[i][j] <= 104
#     0 <= row1 <= row2 < m
#     0 <= col1 <= col2 < n
#     At most 104 calls will be made to sumRegion.

# Accepted
# 328,585
# Submissions
# 617,598

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # Проверяем, что матрица не пуста (m x n)
        if not matrix or not matrix[0]:
            return

        # Получаем размеры матрицы
        m, n = len(matrix), len(matrix[0])

        # Создаем новую матрицу для хранения накопительной суммы
        # Размер новой матрицы будет (m+1) x (n+1) для удобства вычислений
        self.cumSum = [[0] * (n + 1) for _ in range(m + 1)]

        # Заполняем накопительную сумму для каждой ячейки в новой матрице
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Накопительная сумма в точке (i, j) равна сумме текущего элемента матрицы,
                # суммы элементов в предыдущей строке и предыдущем столбце,
                # за вычетом дублирующегося элемента из предыдущей строки и столбца.
                self.cumSum[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.cumSum[i - 1][j]
                    + self.cumSum[i][j - 1]
                    - self.cumSum[i - 1][j - 1]
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Для вычисления суммы элементов в прямоугольнике используем накопительную сумму
        # Накопительная сумма находится в точке (row2 + 1, col2 + 1), исключая (row1, col1).
        # Чтобы получить сумму в прямоугольнике, вычитаем накопительные суммы в "лишних" областях:
        # сумму элементов выше прямоугольника (row1) и слева от прямоугольника (col1),
        # и прибавляем сумму элементов в верхнем левом квадрате (row1, col1), который был вычтен дважды.
        return (
            self.cumSum[row2 + 1][col2 + 1]
            - self.cumSum[row2 + 1][col1]
            - self.cumSum[row1][col2 + 1]
            + self.cumSum[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2


# Тестирование реализации с примером из условия
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3))  # Вывод: 8
print(numMatrix.sumRegion(1, 1, 2, 2))  # Вывод: 11
print(numMatrix.sumRegion(1, 2, 2, 4))  # Вывод: 12


