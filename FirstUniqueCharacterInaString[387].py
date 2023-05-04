# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.
# Accepted
# 1.4M
# Submissions
# 2.3M
# Acceptance Rate
# 59.7%


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
       
       
       
list_s = "leetcode","loveleetcode", "aabb"
for i in list_s:
 Solution.firstUniqChar('Success', i)
