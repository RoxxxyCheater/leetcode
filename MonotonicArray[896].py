# 896. Monotonic Array
# Easy

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true

# Example 2:

# Input: nums = [6,5,4,4]
# Output: true

# Example 3:

# Input: nums = [1,3,2]
# Output: false

 

# Constraints:

#     1 <= nums.length <= 105
#     -105 <= nums[i] <= 105

# Accepted
# 271,878
# Submissions
# 464,661


class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Инициализируем переменные, чтобы отслеживать, является ли массив монотонно возрастающим и убывающим
        increasing = decreasing = True
        
        # Проходимся по массиву, начиная с индекса 1
        for i in range(1, len(nums)):
            # Проверяем, является ли текущий элемент больше предыдущего
            if nums[i] > nums[i - 1]:
                decreasing = False
            # Проверяем, является ли текущий элемент меньше предыдущего
            elif nums[i] < nums[i - 1]:
                increasing = False
        
        # Если либо increasing, либо decreasing равно True, то массив монотонен
        return increasing or decreasing


     
list_num = [1,2,2,3], [6,5,4,4], [1,3,2]
for i in list_num:
    Solution.arrayPairSum("Success", i)
