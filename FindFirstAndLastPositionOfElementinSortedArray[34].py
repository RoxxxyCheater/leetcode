# 34. Find First and Last Position of Element in Sorted Array
# Medium

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

 

# Constraints:

#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     nums is a non-decreasing array.
#     -109 <= target <= 109

# Accepted
# 1,641,124
# Submissions
# 3,865,999




class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Определяем метод класса для поиска начальной и конечной позиции целевого значения
        
        # Функция для поиска начальной позиции целевого значения в отсортированном массиве
        def findStart(nums, target):
            left, right = 0, len(nums) - 1
            start = -1  # Инициализируем начальную позицию значением -1 (если не найдено)
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    start = mid  # Обновляем start, если нашли целевое значение
                    right = mid - 1  # Ищем дальше на левой стороне, исключая текущую позицию
                elif nums[mid] < target:
                    left = mid + 1  # Ищем на правой стороне
                else:
                    right = mid - 1  # Ищем на левой стороне
            return start
        
        # Функция для поиска конечной позиции целевого значения в отсортированном массиве
        def findEnd(nums, target):
            left, right = 0, len(nums) - 1
            end = -1  # Инициализируем конечную позицию значением -1 (если не найдено)
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    end = mid  # Обновляем end, если нашли целевое значение
                    left = mid + 1  # Ищем дальше на правой стороне, исключая текущую позицию
                elif nums[mid] <= target:
                    left = mid + 1  # Ищем на правой стороне
                else:
                    right = mid - 1  # Ищем на левой стороне
            return end
        
        # Вызываем функции поиска начальной и конечной позиции
        start = findStart(nums, target)
        end = findEnd(nums, target)
        
        # Возвращаем результат в виде списка [start, end]
        return [start, end]



list_g = [5,7,7,8,8,10], [5,7,7,8,8,10], []
list_s = 8, 6, 0

for index, list_g in enumerate(list_g):
    Solution.searchRange("Success", list_g, list_s[index])
