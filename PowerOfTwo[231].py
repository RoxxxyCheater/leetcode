# 231. Power of Two
# Easy

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:

# Input: n = 3
# Output: false

 

# Constraints:

#     -231 <= n <= 231 - 1

 
# Follow up: Could you solve it without loops/recursion?
# Accepted
# 1,089,011
# Submissions
# 2,335,852


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n & (n - 1) == 0

ln = 1, 16, 3
for i in ln:
   Solution.isPowerOfTwo('Success', i)
