# 2535. Difference Between Element Sum and Digit Sum of an Array
# Easy

# 555

# 15

# Add to List

# Share
# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

 

# Example 1:

# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Explanation:
# The element sum of nums is 1 + 2 + 3 + 4 = 10.
# The digit sum of nums is 1 + 2 + 3 + 4 = 10.
# The absolute difference between the element sum and digit sum is |10 - 10| = 0.
 

# Constraints:

# 1 <= nums.length <= 2000
# 1 <= nums[i] <= 2000
# Accepted
# 82,001
# Submissions
# 98,084


class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        # Инициализируем переменные для хранения суммы элементов и суммы цифр
        element_sum = 0  # Сумма элементов
        digit_sum = 0    # Сумма цифр
    
        # Итерируемся по элементам массива nums
        for num in nums:
            # Добавляем элемент к сумме элементов
            element_sum += num
    
            # Преобразуем элемент в строку и итерируемся по его символам
            for char in str(num):
                # Преобразуем символ обратно в целое число и добавляем его к сумме цифр
                digit_sum += int(char)
    
        # Рассчитываем абсолютную разницу между суммой элементов и суммой цифр
        absolute_difference = abs(element_sum - digit_sum)
    
        # Возвращаем абсолютную разницу
        return absolute_difference



list_n =  [1,15,6,3], [1,2,3,4]
for i in list_n:
  Solution.differenceOfSum('Success', i)
