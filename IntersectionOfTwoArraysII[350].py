# 350. Intersection of Two Arrays II
# Easy

# 6927

# 915

# Add to List

# Share
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
 

# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# Accepted
# 1,133,361
# Submissions
# 2,015,584

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        intersection = []
        for num, count in counter1.items():
            min_count = min(count, counter2.get(num, 0))
            intersection.extend([num] * min_count)    
        return intersection


list_n1 = [1,2,2,1], [4,9,5]
list_n2 = [2,2], [9,4,9,8,4]

for index, n in enumerate(list_n1):
   Solution.intersect('Success', n, list_n2[index])
