# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Can you find an O(n) solution?
# Accepted
# 419K
# Submissions
# 1.3M
# Acceptance Rate
# 33.2%


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # С помощью множества оставляем уникальные значения
        unique_nums = set(nums)

        # Если в множестве менее 3 элементов, вернуть максимальный элемент
        if len(unique_nums) < 3:
            return max(unique_nums)

        # Удаляем максимальный элемент из множества
        unique_nums.remove(max(unique_nums))

        # Удаляем следующий максимальный элемент из множества
        unique_nums.remove(max(unique_nums))

        # Возвращаем третий максимальный элемент
        return max(unique_nums)
        
list_nums =  [3,2,1],[1,2],[2,2,3,1]
for i in list_nums:
    Solution.thirdMax('Success', i)
