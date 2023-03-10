
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
# Accepted
# 3.1M
# Submissions
# 7.7M
# Acceptance Rate
# 40.3%
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pair:
                unpair_el = stack.pop() if stack else '#'
                if pair[char] != unpair_el:
                    return False
            else:
                stack.append(char)
        return not stack
    
    
list_chars = "()","()[]{}","(]"
for i in list_chars:
   Solution.isValid('Success', i)
