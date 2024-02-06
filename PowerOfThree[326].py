# 326. Power of Three
# Easy

# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

 

# Constraints:

#     -231 <= n <= 231 - 1

 
# Follow up: Could you solve it without loops/recursion?
# Accepted
# 788,718
# Submissions
# 1,705,020

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_pow = 1162261467  # 3^19, the maximum power of three within the constraints
        return n > 0 and max_pow % n == 0 # является ли число n положительным и делится ли максимальная степень тройки max_pow на n без остатка.

ln = 27, 0, -1
 
for i in ln:
   Solution.isPowerOfThree('Success', i)
