# 169. Majority Element
# Easy

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

 

# Constraints:

#     n == nums.length
#     1 <= n <= 5 * 104
#     -109 <= nums[i] <= 109

 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
# Accepted
# 1,853,247
# Submissions
# 2,901,860

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0  # Счетчик для отслеживания количества вхождений текущего кандидата
        candidate = None  # Текущий кандидат на основной элемент

        for num in nums:
            if count == 0:  # Если счетчик равен 0, выбираем нового кандидата
                candidate = num
            if num == candidate:  # Если текущий элемент совпадает с кандидатом, увеличиваем счетчик на 1
                count += 1
            else:  # Если текущий элемент отличается от кандидата, уменьшаем счетчик на 1
                count -= 1

        return candidate  # Возвращаем найденного кандидата в качестве основного элемента

list_n = [3,2,3], [2,2,1,1,1,2,2]
for i in list_n:
   Solution.majorityElement('Success', i)
