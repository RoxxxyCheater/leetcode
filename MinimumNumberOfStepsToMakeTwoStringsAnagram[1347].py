# 1347. MinimumNumberOfStepsToMakeTwoStringsAnagram
# Medium
# 2K
# 80
# Companies
# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

# Example 1:

# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
# Example 2:

# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
# Example 3:

# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams. 
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s.length == t.length
# s and t consist of lowercase English letters only.
# Accepted
# 144.7K
# Submissions
# 184.9K
# Acceptance Rate
# 78.2%
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) != len(t):
            raise ValueError("Input strings must have the same length.")   
        freq_s = {}
        freq_t = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        steps = 0
        for char, count in freq_s.items():
            if char in freq_t:
                steps += max(0, count - freq_t[char])
            else:
                steps += count    
        return steps

list_s = "bab", "leetcode", "anagram"
list_t = "aba", "practice", "mangaar"
for t, s in enumerate(list_s):
   Solution.minSteps('Success', s, list_t[t])
