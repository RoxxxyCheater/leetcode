# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

# Constraints:

#     1 <= haystack.length, needle.length <= 104
#     haystack and needle consist of only lowercase English characters.

# Accepted
# 1.6M
# Submissions
# 4.2M
# Acceptance Rate
# 38.7%
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)        
        # if not needle:
        #     return 0
        
        # n = len(needle)
        # for i in range(len(haystack) - n + 1):
        #     if haystack[i:i+n] == needle:
        #         return i
        
        # return -1
    
list_needle = "sad", "leeto"
list_haystack = "leetcode",'sadbutsad'
for index, strs in enumerate(list_needle):
        Solution('Success', haystack[index], strs)

