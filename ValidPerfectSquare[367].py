# 367. Valid Perfect Square
# Easy

# 3739

# 284

# Add to List

# Share
# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

# Constraints:

# 1 <= num <= 231 - 1
# Accepted
# 500,814
# Submissions
# 1,155,148


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
    
        left, right = 1, num // 2
    
        while left <= right:
            mid = left + (right - left) // 2  # Вычисляем середину диапазона для бинарного поиска
            square = mid * mid  # Вычисляем квадрат числа mid
    
            if square == num:  # Если квадрат числа равен num, то num является точным квадратом
                return True
            elif square < num:  # Если квадрат числа меньше num, ищем в правой половине диапазона
                left = mid + 1
            else:  # Если квадрат числа больше num, ищем в левой половине диапазона
                right = mid - 1
    
        return False  # Если не нашли точный квадрат, возвращаем False

list_n = 16, 14
for i in list_n:
   Solution.isPerfectSquare('Success', i)
