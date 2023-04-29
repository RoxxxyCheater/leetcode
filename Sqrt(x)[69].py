
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

#     For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

# Constraints:

#     0 <= x <= 231 - 1

# Accepted
# 1.4M
# Submissions
# 3.9M
# Acceptance Rate
# 37.5%

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while True:
            mid = (left + right) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                if (mid + 1) > x / (mid + 1):
                    return mid
                left = mid + 1
    
list_x = 4,8
for i in list_x:
 Solution.mySqrt('Success', i)
