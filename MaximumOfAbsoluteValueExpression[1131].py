# 1131. Maximum of Absolute Value Expression
# Medium

# Given two arrays of integers with equal lengths, return the maximum value of:

# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

# where the maximum is taken over all 0 <= i, j < arr1.length.

 

# Example 1:

# Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# Output: 13

# Example 2:

# Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
# Output: 20

 

# Constraints:

#     2 <= arr1.length == arr2.length <= 40000
#     -10^6 <= arr1[i], arr2[i] <= 10^6

# Accepted
# 22,603
# Submissions
# 46,740


class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        max_val = 0  # Инициализация переменной для хранения максимального значения выражения
        for sign1 in [-1, 1]:  # Перебор всех возможных значений знаков для arr1[i]
            for sign2 in [-1, 1]:  # Перебор всех возможных значений знаков для arr2[i]
                min_arr = float('inf')  # Инициализация переменной для хранения минимального значения выражения
                max_arr = float('-inf')  # Инициализация переменной для хранения максимального значения выражения
                for i in range(len(arr1)):  # Перебор всех элементов массивов arr1 и arr2
                    cur_val = sign1 * arr1[i] + sign2 * arr2[i] + i  # Вычисление текущего значения выражения
                    min_arr = min(min_arr, cur_val)  # Обновление минимального значения
                    max_arr = max(max_arr, cur_val)  # Обновление максимального значения
                max_val = max(max_val, max_arr - min_arr)  # Обновление максимального значения выражения
        return max_val  # Возврат максимального значения выражения

arr = [1,2,3,4], [1,-2,-5,0,10]
arr2 = [-1,4,5,6], [0,-2,-1,-7,-4]

for a2, a1 in enumerate(arr):
    Solution.maxAbsValExpr('Success', a1, arr2[a2])
