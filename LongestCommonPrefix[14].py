# 14. Longest Common Prefix
# Easy
# 12.4K
# 3.7K
# Companies

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

 

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.

# Accepted
# 2.2M
# Submissions
# 5.3M
# Acceptance Rate
# 40.8%
list_str = ["a"],["cir","car"],["ab", "a"],["flower","flow","flight"],[""], ["dog","racecar","car"] , ["bluedog","blueracecar","bluscar"]
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return "".join([word[0] if len(set(word))==1 else '.' for word in zip(*strs)]).split('.')[0]

for i in list_str:
    Solution.longestCommonPrefix("Success", i)
