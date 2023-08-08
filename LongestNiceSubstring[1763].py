# 1763. Longest Nice Substring
# Easy

# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

# Example 1:

# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.

# Example 2:

# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

# Example 3:

# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.

 

# Constraints:

#     1 <= s.length <= 100
#     s consists of uppercase and lowercase English letters.

# Accepted
# 41,497
# Submissions
# 68,162
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_nice(start, end):
            seen = set()
            for i in range(start, end + 1):
                seen.add(s[i])

            for char in seen:
                if char.lower() not in seen or char.upper() not in seen:
                    return False
            return True

        longest = ""
        for i in range(len(s)):
            for j in range(i + len(longest), len(s)):
                if is_nice(i, j):
                    longest = s[i:j + 1]
        return longest
