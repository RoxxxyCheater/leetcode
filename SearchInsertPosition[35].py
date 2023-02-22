# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

 

# Constraints:

#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums contains distinct values sorted in ascending order.
#     -104 <= target <= 104

# Accepted
# 2M
# Submissions
# 4.6M
# Acceptance Rate
# 42.5%
list_nums = [1,3,5,6]
lest_target = 5,2, 7
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index,num in enumerate(nums):
            if target < num: return index
            if num == target: return index
        return len(nums)
       
#         for  index,num in enumerate(nums):
#             if target == num:
#                 return index
#         if target not in nums:
#             nums.append(target)
#             nums.sort()
#         return nums.index(target)


for i in lest_target:
    Solution.searchInsert("Success", list_nums, i)
