# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
#nums = list(input("Enter the list of numbers: ").split(','))
 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

        #  """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """

# Constraints: sum(s)

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.

 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
nums = [2,7,11,15]#[3,2,4]#[3,3]#
from time import perf_counter
class Solution(object):
    def twoSum(self, nums, target): 
        res_list = {}
        for index, num in enumerate(nums):
            result = target - num
            print(result, index)
            if result in res_list: return [res_list[result], index]
            res_list[num] = index

if __name__ == '__main__':

    start = perf_counter()
    Solution.twoSum(nums,nums,target =9)
    print(f"time: {(perf_counter()-start):.02f}")