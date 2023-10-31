# 2206. Divide Array Into Equal Pairs
# Easy

# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

#     Each element belongs to exactly one pair.
#     The elements present in a pair are equal.

# Return true if nums can be divided into n pairs, otherwise return false.

 

# Example 1:

# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation: 
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: 
# There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

 

# Constraints:

#     nums.length == 2 * n
#     1 <= n <= 500
#     1 <= nums[i] <= 500

# Accepted
# 65,330
# Submissions
# 89,191


class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Сортируем массив
        nums.sort()
    
        # Проверяем, равны ли соседние элементы
        for i in range(0, len(nums), 2):
            # Проверяем каждую пару (элементы на четных и нечетных индексах)
            if nums[i] != nums[i + 1]:
                # Если пара не равных элементов, то возвращаем False
                return False
    
        # Если прошли все проверки и не нашли пару, в которой элементы не равны,
        # то возвращаем True, что значит можно разделить массив на пары
        return True



list_n = [3,2,3,2,2,2], [1,2,3,4]
for i in list_n:
  Solution.divideArray('Success', i)
 
