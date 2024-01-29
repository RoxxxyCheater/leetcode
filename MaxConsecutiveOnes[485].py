# 485. Max Consecutive Ones
# Easy

# 5475

# 451

# Add to List

# Share
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Accepted
# 1,060,462
# Submissions
# 1,817,040


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consecutive_ones = 0  # Переменная для хранения максимального числа последовательных единиц
        current_consecutive_ones = 0  # Переменная для хранения текущего числа последовательных единиц

        for num in nums:  # Проходим по массиву чисел
            if num == 1:  # Если текущее число равно 1
                current_consecutive_ones += 1  # Увеличиваем текущее число последовательных единиц на 1
                max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)  # Обновляем максимальное число последовательных единиц
            else:  # Если текущее число не равно 1 (равно 0)
                current_consecutive_ones = 0  # Обнуляем текущее число последовательных единиц

        return max_consecutive_ones  # Возвращаем максимальное число последовательных единиц



l_n = [1,1,0,1,1,1], [1,0,1,1,0,1]
for i in l_n:
   Solution.findMaxConsecutiveOnes('Success', i)
