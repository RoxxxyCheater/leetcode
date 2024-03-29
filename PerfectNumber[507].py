# 507. Perfect Number
# Easy

# 1021

# 1203

# Add to List

# Share
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

 

# Example 1:

# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# Example 2:

# Input: num = 7
# Output: false
 

# Constraints:

# 1 <= num <= 108
# Accepted
# 167,584
# Submissions
# 426,092


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False  # Число меньше или равно 1 не может быть совершенным
    
        divisor_sum = 1  # 1 всегда является делителем
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisor_sum += i  # Добавляем делитель
                if i != num // i:  # Избегаем учета одного и того же делителя дважды для квадратов
                    divisor_sum += num // i  # Добавляем соответствующий делитель
    
        return divisor_sum == num  # Возвращаем True, если сумма делителей равна исходному числу


l_n = 28,7

for n in l_n:
   Solution.checkPerfectNumber('Success', n)
