# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

# Constraints:

#     -231 <= x <= 231 - 1

 
# Follow up: Could you solve it without converting the integer to a string?
# Accepted
# 2.9M
# Submissions
# 5.4M
# Acceptance Rate
# 53.3%
list_num = [121,-121, 10]

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            reversed_num = int(str(x)[::-1])
            return True if x == reversed_num else False

for i in list_num:
    Solution.isPalindrome("Success", i)