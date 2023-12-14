# 2186. Minimum Number of Steps to Make Two Strings Anagram II
# Medium

# 516

# 18

# Add to List

# Share
# You are given two strings s and t. In one step, you can append any character to either s or t.

# Return the minimum number of steps to make s and t anagrams of each other.

# An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

# Example 1:

# Input: s = "leetcode", t = "coats"
# Output: 7
# Explanation: 
# - In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
# - In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
# "leetcodeas" and "coatsleede" are now anagrams of each other.
# We used a total of 2 + 5 = 7 steps.
# It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
# Example 2:

# Input: s = "night", t = "thing"
# Output: 0
# Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps.
 

# Constraints:

# 1 <= s.length, t.length <= 2 * 105
# s and t consist of lowercase English letters.
# Accepted
# 36,705
# Submissions
# 51,020


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        freq_s = {}
        freq_t = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        steps = 0
        for char in set(s + t):
            steps += abs(freq_s.get(char, 0) - freq_t.get(char, 0))
        return steps


list_s = "leetcode", "night"
list_t = "coats", "thing"

for t, s in enumerate(list_s):
    Solution.minSteps("Success", s, list_t[t])
