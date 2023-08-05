# 50. Pow(x, n)
# Medium

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

 

# Constraints:

#     -100.0 < x < 100.0
#     -231 <= n <= 231-1
#     n is an integer.
#     Either x is not zero or n > 0.
#     -104 <= xn <= 104

# Accepted
# 1,339,472
# Submissions
# 3,950,029
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        def helper(x, n):
            if n == 1:
                return x

            half_pow = helper(x, n // 2)
            if n % 2 == 0:
                return half_pow * half_pow
            else:
                return half_pow * half_pow * x

        return helper(x, n)


list_x = 2.00000, 2.10000, 2.00000
list_n = 10, 3, -2
