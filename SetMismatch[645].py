# 645. Set Mismatch
# Easy

# 3840

# 890

# Add to List

# Share
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104
# Accepted
# 281,875
# Submissions
# 663,076

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq_dict = {}  # Словарь для хранения частоты чисел
        
        # Вычисляем частоту каждого числа в массиве nums
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        duplicate = None  # Переменная для хранения повторяющегося числа
        missing = None    # Переменная для хранения пропущенного числа
        # Проходимся по числам от 1 до длины массива nums
        for num in range(1, len(nums) + 1):
            if num in freq_dict:
                if freq_dict[num] == 2:
                    duplicate = num  # Если частота числа равна 2, это повторяющееся число
                elif freq_dict[num] == 0:
                    missing = num    # Если частота числа равна 0, это пропущенное число
            else:
                missing = num
        
        return [duplicate, missing]
     
list_n = [1,2,2,4], [1,1]
for i in list_n:
   Solution.findErrorNums('Success', i)
