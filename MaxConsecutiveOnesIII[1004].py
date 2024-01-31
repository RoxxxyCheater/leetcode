# 1004. Max Consecutive Ones III
# Medium

# 8085

# 106

# Add to List

# Share
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
# Accepted
# 444,945
# Submissions
# 710,456


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0  # Левая граница текущего окна
        max_length = 0  # Максимальная длина последовательности единиц
        zero_count = 0  # Количество нулей в текущем окне
    
        for right in range(len(nums)):  # Проходим по массиву nums
            if nums[right] == 0:  # Если текущий элемент равен 0
                zero_count += 1  # Увеличиваем счетчик нулей
    
            while zero_count > k:  # Если количество нулей в текущем окне превышает k
                if nums[left] == 0:  # Если крайний левый элемент текущего окна равен 0
                    zero_count -= 1  # Уменьшаем счетчик нулей
                left += 1  # Сдвигаем левую границу окна
    
            max_length = max(max_length, right - left + 1)  # Обновляем максимальную длину последовательности единиц
    
        return max_length  # Возвращаем максимальную длину последовательности единиц




list_n = [1,1,1,0,0,0,1,1,1,1,0], [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
list_k = 2,3

for i, n in enumerate(list_n):
    Solution.longestOnes("Success", n, list_k[i])
