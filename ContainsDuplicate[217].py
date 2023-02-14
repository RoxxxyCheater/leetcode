# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

 

# Constraints:

#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109

# Accepted
# 2.5M
# Submissions
# 4.1M
# Acceptance Rate
# 61.4%

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = set()
        for num in nums:
            if num in res: 
                return True
            else:
                res.add(num)


list_nums = [1,2,3,4],[1,2,3,1],[1,1,1,3,3,4,3,2,4,2]
for i in list_nums:
    Solution.containsDuplicate('Success', i)