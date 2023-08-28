# 287. Find the Duplicate Number
# Medium

# 20045

# 3144

# Add to List

# Share
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
# Accepted
# 1,238,138
# Submissions
# 2,097,527

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        # Фаза 1: Нахождение точки пересечения двух указателей
        slow = nums[0]  # Медленный указатель начинает с первого элемента
        fast = nums[0]  # Быстрый указатель также начинает с первого элемента
        
        # Перемещение медленного указателя на один шаг и быстрого указателя на два шага
        while True:
            slow = nums[slow]           # Медленный указатель двигается на следующий элемент
            fast = nums[nums[fast]]     # Быстрый указатель двигается на элемент через один
            if slow == fast:
                break  # Если медленный и быстрый указатели столкнулись, выходим из цикла
        
        # Фаза 2: Нахождение входа в цикл (повторяющегося числа)
        slow = nums[0]  # Медленный указатель начинает с первого элемента
        while slow != fast:
            slow = nums[slow]  # Оба указателя двигаются на один шаг
            fast = nums[fast]  # пока не встретятся в точке входа в цикл
        
        return slow  # Возвращаем найденную точку входа в цикл


list_prices = [1,3,4,2,2], [3,1,3,4,2]
for i in list_prices:
   Solution.findDuplicate('Success', i)
