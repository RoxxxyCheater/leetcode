# 697. Degree of an Array
# Easy

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

 

# Constraints:

#     nums.length will be between 1 and 50,000.
#     nums[i] will be an integer between 0 and 49,999.

# Accepted
# 191,534
# Submissions
# 341,604



class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_info = {}  # Словарь для хранения информации о каждом элементе
        max_degree = 0  # Максимальная степень (максимальное количество появлений элемента)
        min_length = len(nums)  # Начальная минимальная длина подмассива

        for i, num in enumerate(nums):
            if num in element_info:
                # Если элемент уже встречался, обновляем индекс последнего появления
                element_info[num][1] = i
                element_info[num][2] += 1
            else:
                # Если элемент встречается впервые, добавляем его в словарь
                element_info[num] = [i, i, 1]

            max_degree = max(max_degree, element_info[num][2])

        for num, info in element_info.items():
            if info[2] == max_degree:
                # Для элементов с максимальной степенью вычисляем длину подмассива
                min_length = min(min_length, info[1] - info[0] + 1)

        return min_length
     
list_n = [1,2,2,3,1], [1,2,2,3,1,4,2]

for i in list_n:
  Solution.findShortestSubArray('Success', i)
