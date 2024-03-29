# 349. Intersection of Two Arrays
# Easy

# 5372

# 2210

# Add to List

# Share
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# Accepted
# 952,984
# Submissions
# 1,325,899


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Используем set для уникальных значений в каждом массиве
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
    
        # Используем оператор & для нахождения пересечения множеств
        result_set = set_nums1 & set_nums2
    
        # Преобразуем результат в список
        result_list = list(result_set)
    
        return result_list

list_n = [1,2,2,1], [4,9,5]
list_ nn = [9,4,9,8,4], [2,2]

for index, n in enumerate(list_n):
    Solution.intersection('Success', n, list_nn[index])
