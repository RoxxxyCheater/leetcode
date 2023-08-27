# 34. Find First and Last Position of Element in Sorted Array
# Medium

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

 

# Constraints:

#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     nums is a non-decreasing array.
#     -109 <= target <= 109

# Accepted
# 1,641,124
# Submissions
# 3,865,999




class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findStart(nums, target):
            left, right = 0, len(nums) - 1
            start = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    start = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return start
        
        def findEnd(nums, target):
            left, right = 0, len(nums) - 1
            end = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    end = mid
                    left = mid + 1
                elif nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return end
        
        start = findStart(nums, target)
        end = findEnd(nums, target)
        
        return [start, end]



list_g = [5,7,7,8,8,10], [5,7,7,8,8,10], []
list_s = 8, 6, 0

for index, list_g in enumerate(list_g):
    Solution.searchRange("Success", list_g, list_s[index])
