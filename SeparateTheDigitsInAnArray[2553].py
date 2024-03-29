# 2553. SeparateTheDigitsInAnArray
# Easy

# 369

# 12

# Add to List

# Share
# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

# To separate the digits of an integer is to get all the digits it has in the same order.

# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
 

# Example 1:

# Input: nums = [13,25,83,77]
# Output: [1,3,2,5,8,3,7,7]
# Explanation: 
# - The separation of 13 is [1,3].
# - The separation of 25 is [2,5].
# - The separation of 83 is [8,3].
# - The separation of 77 is [7,7].
# answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
# Example 2:

# Input: nums = [7,1,3,9]
# Output: [7,1,3,9]
# Explanation: The separation of each integer in nums is itself.
# answer = [7,1,3,9].
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 105
# Accepted
# 46,658
# Submissions
# 59,250
class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []  # Создаем пустой список для хранения результата
        for num in nums:  # Итерируемся по каждому числу в массиве nums
            num_str = str(num)  # Преобразуем число в строку, чтобы разделить его на цифры
            digits = [int(digit) for digit in num_str]  # Создаем список цифр, конвертируя каждый символ строки обратно в целое число
            answer.extend(digits)  # Добавляем цифры к списку ответа, сохраняя порядок
        return answer 

list_n = [13,25,83,77], [7,1,3,9]
for i in list_n:
    Solution.separateDigits('Success', i)
