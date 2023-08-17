# 976. Largest Perimeter Triangle
# Easy

# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

# Example 2:

# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

 

# Constraints:

#     3 <= nums.length <= 104
#     1 <= nums[i] <= 106

# Accepted
# 213,932
# Submissions
# 389,589


class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Сортируем массив в порядке убывания
        for i in range(len(nums) - 2):
            # Проверяем все тройки чисел, начиная с текущего индекса `i`
            if nums[i] < nums[i + 1] + nums[i + 2]:
                # Если текущие три числа могут образовать треугольник,
                # то возвращаем их сумму, которая будет периметром треугольника
                return nums[i] + nums[i + 1] + nums[i + 2]
        # Если не удалось найти треугольник с ненулевой площадью,
        # то возвращаем 0
        return 0

list_n = [2,1,2], [1,2,1,10]
for i in list_n:
  Solution.largestPerimeter('Success', i)
