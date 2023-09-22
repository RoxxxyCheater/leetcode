# 1748. Sum of Unique Elements
# Easy

# 1384

# 34

# Add to List

# Share
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

 

# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# Accepted
# 133,358
# Submissions
# 174,001

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        unique_sum = 0
        for num, count in count_dict.items():
            if count == 1:
                unique_sum += num

        return unique_sum



list_n = [1,2,3,2], [1,1,1,1,1], [1,2,3,4,5]
for i in list_n:
   Solution.sumOfUnique('Success', i)
