# 1991. Find the Middle Index in Array
# Easy

# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

# If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

 

# Example 1:

# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

# Example 2:

# Input: nums = [1,-1,4]
# Output: 2
# Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
# The sum of the numbers after index 2 is: 0

# Example 3:

# Input: nums = [2,5]
# Output: -1
# Explanation: There is no valid middleIndex.

 

# Constraints:

#     1 <= nums.length <= 100
#     -1000 <= nums[i] <= 1000

 

# Note: This question is the same as 724: https://leetcode.com/problems/find-pivot-index/
# Accepted
# 68,326
# Submissions
# 101,599
class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0  # Индекс левой части массива
        right = sum(nums[1:])  # Сумма элементов правой части массива, исключая первый элемент
        for i in range(len(nums)):
            if left == right:  # Если сумма левой части равна сумме правой части
                return i  # Возвращаем текущий индекс как левый центральный индекс
            if i < len(nums) - 1:
                left += nums[i]  # Увеличиваем сумму левой части на текущий элемент
                right -= nums[i + 1]  # Уменьшаем сумму правой части на следующий элемен
        return -1  # Если левый центральный индекс не найден, возвращаем -1

list_n =  [2,3,-1,8,4],[1,-1,4],[2,5]
for i in list_n:
  Solution.findMiddleIndex('Success', i)
