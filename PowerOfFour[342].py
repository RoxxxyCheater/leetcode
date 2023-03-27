# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?
# Accepted
# 448.8K
# Submissions
# 973.2K
# Acceptance Rate
# 46.1%
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n <= 0 else log(n, 4).is_integer()
      
list_nums = 16,5,1
for i in list_nums:
  Solution.isPowerOfFour('Success', i)
