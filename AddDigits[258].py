# 258. Add Digits
# Easy

# 4387

# 1894

# Add to List

# Share
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0
 

# Constraints:

# 0 <= num <= 231 - 1
 

# Follow up: Could you do it without any loop/recursion in O(1) runtime?

# Accepted
# 678,476
# Submissions
# 1,029,965
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Если число равно 0, то его цифровой корень также равен 0
        if num == 0:
            return 0
        # Используем формулу для вычисления цифрового корня
        # Цифровой корень равен 1 плюс остаток от деления (num - 1) на 9
        return 1 + (num - 1) % 9

list_n = 38, 0
for i in list_n:
   Solution.addDigits('Success', i)
