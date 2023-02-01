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
list_str = ["flower","flow","flight"] , ["dog","racecar","car"] , ["bluedog","blueracecar","bluscar"]
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = []
        print(len(strs))
        a,b,c = (' '.join(strs)).split(" ")
        print("abc: ", len(''.join(strs)))
        for index,letter in enumerate(min(strs, key=len)):
            if a[index] == b[index] == c[index]:
                pre.append(a[index])
                print("==letter: ", a[index],b[index],c[index], letter)
            else:
                print("!=letter: ", a[index],b[index],c[index])
        return "" if not pre else ''.join(pre)

for i in list_str:
    Solution.longestCommonPrefix("Success", i)