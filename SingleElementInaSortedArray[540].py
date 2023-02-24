# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

 

# Constraints:

#     1 <= nums.length <= 105
#     0 <= nums[i] <= 105

# Accepted
# 443.5K
# Submissions
# 749.5K
# Acceptance Rate
# 59.2%

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for index in range(0,len(nums)- 1, 2):
            if nums[index] != nums[index+1]:return nums[index]
        return -1



list_nums = [1,1,2,3,3,4,4,8,8], [3,3,7,7,10,11,11]
for i in list_nums:
    Solution.singleNonDuplicate('Success', i)


# TimeLimit
        # uniq = set(nums) 
        # return [i for i in uniq if nums.count(i) == 1][0]

        # uniq = set(nums) 
        # for i in uniq:
        #     if nums.count(i) == 1: return i
