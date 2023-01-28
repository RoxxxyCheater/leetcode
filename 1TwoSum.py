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
nums = [3,2,4]#[3,3]#[2,7,11,15]#
class Solution(object):
    def twoSum(self, nums, target): 
        for i in range(len(nums)):
            for j in range(len(nums[::-1])):
                if target == nums[i] + nums[::-1][j] and i != nums.index(nums[::-1][j]):
                    print('Sum: ',nums[i] + nums[::-1][j], 'Target: ', target)
                    print(i,nums.index(nums[::-1][j]))
                    return i,nums.index(nums[::-1][j])
                else:
                    print('NOT Succsess')
        #nums.pop(i)
        return True

Solution.twoSum(nums,nums,target =6)