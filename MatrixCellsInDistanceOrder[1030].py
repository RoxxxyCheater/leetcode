# 1030. Matrix Cells in Distance Order
# Easy

# You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

# Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

# The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

 

# Example 1:

# Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
# Output: [[0,0],[0,1]]
# Explanation: The distances from (0, 0) to other cells are: [0,1]

# Example 2:

# Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
# Output: [[0,1],[0,0],[1,1],[1,0]]
# Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
# The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

# Example 3:

# Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

# Constraints:

#     1 <= rows, cols <= 100
#     0 <= rCenter < rows
#     0 <= cCenter < cols

# Accepted
# 52,837
# Submissions
# 75,453
class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        # Создаем список для хранения координат ячеек вместе с их расстояниями.
        cell_distances = []
    
        # Перебираем все ячейки в матрице.
        for r in range(rows):
            for c in range(cols):
                # Рассчитываем расстояние от текущей ячейки до центра.
                distance = abs(r - rCenter) + abs(c - cCenter)
                # Добавляем координаты ячейки и ее расстояние в виде кортежа.
                cell_distances.append((r, c, distance))
    
        # Сортируем список cell_distances на основе расстояния (третий элемент кортежа).
        cell_distances.sort(key=lambda x: x[2])
    
        # Извлекаем и возвращаем отсортированные координаты ячеек без расстояний.
        return [[r, c] for r, c, _ in cell_distances]
     
rows = 1,2,2
cols = 2,2,3
rCenter = 0,0,1
cCenter = 0,1,2
for index, row in enumerate(rows):
   Solution.addToArrayForm('Success', row, cols[index], rCenter[index], cCenter[index])
