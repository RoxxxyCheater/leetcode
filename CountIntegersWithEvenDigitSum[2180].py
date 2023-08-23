# 2180. Count Integers With Even Digit Sum
# Easy

# 536

# 24

# Add to List

# Share
# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

# The digit sum of a positive integer is the sum of all its digits.

 

# Example 1:

# Input: num = 4
# Output: 2
# Explanation:
# The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
# Example 2:

# Input: num = 30
# Output: 14
# Explanation:
# The 14 integers less than or equal to 30 whose digit sums are even are
# 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
 

# Constraints:

# 1 <= num <= 1000
# Accepted
# 47,469
# Submissions
# 71,976

class Solution(object):
    """
    :type num: int
    :rtype: int
    """
    def countEven(self, num):
        count = 0
        for i in range(1, num + 1):
            if self.is_even_digit_sum(i):
                count += 1
        return count
    
    def is_even_digit_sum(self,n):
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        return digit_sum % 2 == 0




list_n = 4,30
for i in list_n:
    Solution.countEven('Success', i)
