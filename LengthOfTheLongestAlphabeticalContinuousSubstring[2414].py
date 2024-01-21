# 2414. Length of the Longest Alphabetical Continuous Substring
# Medium

# 476

# 29

# Add to List

# Share
# An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

# For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
# Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

 

# Example 1:

# Input: s = "abacaba"
# Output: 2
# Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
# "ab" is the longest continuous substring.
# Example 2:

# Input: s = "abcde"
# Output: 5
# Explanation: "abcde" is the longest continuous substring.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only English lowercase letters.
# Accepted
# 41,606
# Submissions
# 72,150


class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_length = 1 
        current_length = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        max_length = max(max_length, current_length)
        return max_length

l_s = "abacaba", "abcde"

for i in l_s:
   Solution.longestContinuousSubstring('Success', i)
