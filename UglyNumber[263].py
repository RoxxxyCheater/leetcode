v# 263. Ugly Number
# Easy

# 2922

# 1546

# Add to List

# Share
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
 

# Constraints:

# -231 <= n <= 231 - 1
# Accepted
# 435,467
# Submissions
# 1,033,509
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False  # Число должно быть положительным, поэтому возвращаем False, если n меньше или равно 0.
        prime_factors = [2, 3, 5]  # Потенциальные простые делители
        for factor in prime_factors:
            while n % factor == 0:
                n //= factor  # Целочисленное деление n на текущий простой делитель, пока оно делится нацело.
        return n == 1  # Если после всех делений получается 1, то исходное число является уродливым.
     
        # if n <= 0:
        #     return False  # Число должно быть положительным, поэтому возвращаем False, если n меньше или равно 0.
        # while n % 2 == 0:
        #     n /= 2  # Делаем целочисленное деление n на 2 до тех пор, пока оно делится нацело.
        # while n % 3 == 0:
        #     n /= 3  # Делаем целочисленное деление n на 3 до тех пор, пока оно делится нацело.
        # while n % 5 == 0:
        #     n /= 5  # Делаем целочисленное деление n на 5 до тех пор, пока оно делится нацело.
        # return n == 1  # Если после всех делений получается 1, то исходное число является уродливым.
         
list_num = 6, 1, 14
for i in list_num:
  Solution.isUgly('Success', i)
