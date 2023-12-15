# 2006. Count Number of Pairs With Absolute Difference K
# Easy

# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

#     x if x >= 0.
#     -x if x < 0.

 

# Example 1:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]

# Example 2:

# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.

# Example 3:

# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]

 

# Constraints:

#     1 <= nums.length <= 200
#     1 <= nums[i] <= 100
#     1 <= k <= 99

# Accepted
# 115,053
# Submissions
# 138,632


class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        # Создаем словарь для хранения количества встреченных чисел
        num_count = {}
        count = 0  # Переменная для подсчета пар чисел с разницей k
        
        # Итерируем по массиву чисел
        for num in nums:
            # Проверяем, есть ли число num - k в словаре, и увеличиваем count соответственно
            if num - k in num_count:
                count += num_count[num - k]
            
            # Проверяем, есть ли число num + k в словаре и k > 0 (избегаем учета одинаковых чисел)
            if num + k in num_count and k > 0:
                count += num_count[num + k]
            
            # Обновляем словарь num_count, увеличивая счетчик для текущего числа
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        return count
     
list_nums = [1,2,2,1], [1,3], [3,2,1,5,4]
k = 2, 3, 1
for index, num in enumerate(list_nums):
    Solution.countKDifference('Success', num, k[index])
