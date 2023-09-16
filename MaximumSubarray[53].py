# 53. Maximum Subarray
# Medium

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

 

# Constraints:

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104

 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
# Accepted
# 3,395,332
# Submissions
# 6,747,749


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]  # Переменная для хранения максимальной суммы
        current_sum = nums[0]  # Переменная для хранения текущей суммы

        for i in range(1, len(nums)):
            # Выбираем максимум из текущего элемента и суммы текущего элемента с предыдущей суммой
            current_sum = max(nums[i], current_sum + nums[i])
            # Обновляем максимальную сумму
            max_sum = max(max_sum, current_sum)

        return max_sum

list_n = [-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]
for i in list_n:
   Solution.maxSubArray('Success', i)
