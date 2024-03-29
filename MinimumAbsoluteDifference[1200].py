# 1200. Minimum Absolute Difference
# Easy

# 2256

# 72

# Add to List

# Share
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
 

# Constraints:

# 2 <= arr.length <= 105
# -106 <= arr[i] <= 106
# Accepted
# 173,720
# Submissions
# 250,124


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()  # Сортируем массив в порядке возрастания
    
        min_diff = float('inf')  # Инициализируем min_diff бесконечностью
    
        result = []  # Создаем пустой список для хранения пар
    
        # Находим минимальную абсолютную разницу между элементами
        for i in range(1, len(arr)):  # Проходим по всем элементам массива, начиная с первого
            diff = arr[i] - arr[i - 1]  # Вычисляем разницу между текущим и предыдущим элементами
            if diff < min_diff:  # Если разница меньше текущей минимальной разницы
                min_diff = diff  # Обновляем минимальную разницу
    
        # Находим пары с минимальной абсолютной разницей
        for i in range(1, len(arr)):  # Проходим по всем элементам массива, начиная с первого
            diff = arr[i] - arr[i - 1]  # Вычисляем разницу между текущим и предыдущим элементами
            if diff == min_diff:  # Если разница равна минимальной разнице
                result.append([arr[i - 1], arr[i]])  # Добавляем пару в результат
    
        return result  # Возвращаем список пар



list_a = [4,2,1,3],[1,3,6,10,15],[3,8,-10,23,19,-4,-14,27]
for i in list_a:
   Solution.minimumAbsDifference('Success', i)

