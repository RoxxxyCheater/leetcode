# 378. Kth Smallest Element in a Sorted Matrix
# Medium

# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5

 

# Constraints:

#     n == matrix.length == matrix[i].length
#     1 <= n <= 300
#     -109 <= matrix[i][j] <= 109
#     All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
#     1 <= k <= n2

 

# Follow up:

#     Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
#     Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

# Accepted
# 570,935
# Submissions
# 919,727

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)  # Получаем размер матрицы (предполагается, что матрица квадратная)
        left, right = matrix[0][0], matrix[n - 1][n - 1]  # Инициализируем левую и правую границы для бинарного поиска
        
        while left < right:  # Выполняем бинарный поиск, пока левая граница меньше правой
            mid = left + (right - left) // 2  # Вычисляем среднее значение текущего диапазона
            count = 0  # Инициализируем счетчик числа элементов меньше или равных mid
            j = n - 1  # Начинаем с самой правой колонки
            
            for i in range(n):  # Проходим по каждой строке матрицы
                while j >= 0 and matrix[i][j] > mid:  # Поиск элемента, меньшего или равного mid
                    j -= 1
                count += (j + 1)  # Увеличиваем счетчик на количество элементов в текущей строке меньших или равных mid
            
            if count < k:  # Если число элементов меньше k, сдвигаем левую границу
                left = mid + 1
            else:  # В противном случае сдвигаем правую границу
                right = mid
        
        return left  # Возвращаем значение left как k-тое наименьшее число



list_m = [[1,5,9],[10,11,13],[12,13,15]], [[-5]]
list_k = 8, 1
for index, m in enumerate(list_m):
   Solution.kthSmallest('Success', m, list_k[index])

