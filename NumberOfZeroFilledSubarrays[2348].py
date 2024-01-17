# 2348. Number of Zero-Filled Subarrays
# Medium

# 2196

# 74

# Add to List

# Share
# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
# Example 2:

# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
# Example 3:

# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Accepted
# 118,325
# Submissions
# 177,433


class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Инициализация переменных
        count_zeros = 0  # Счетчик последовательных нулей
        result = 0       # Переменная для хранения общего количества подмассивов с нулями
    
        # Итерация по массиву
        for num in nums:
            if num == 0:
                count_zeros += 1  # Увеличиваем счетчик нулей при обнаружении нулевого элемента
                result += count_zeros  # Обновляем результат на основе количества нулей
            else:
                count_zeros = 0  # Если встречен ненулевой элемент, обнуляем счетчик
    
        return result

l_n = [1,3,0,0,2,0,0,4], [0,0,0,2,0,0], [2,10,2019]

for n in l_n:
   Solution.zeroFilledSubbarray('Success', n)
