# 1790. Check if One String Swap Can Make Strings Equal
# Easy

# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.

# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.

 

# Constraints:

#     1 <= s1.length, s2.length <= 100
#     s1.length == s2.length
#     s1 and s2 consist of only lowercase English letters.

# Accepted
# 96,375
# Submissions
# 212,239


class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        diff_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]
        return False 


s1 = "bank", "attack", "kelb"
s2 = "defend","kanb", "kelb"

for i, s in enumerate(s1):
   Solution.areAlmostEqual('Success', s, s2[i])
