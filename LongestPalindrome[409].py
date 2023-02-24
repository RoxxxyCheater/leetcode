# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

 

# Constraints:

#     1 <= s.length <= 2000
#     s consists of lowercase and/or uppercase English letters only.

# Accepted
# 476.2K
# Submissions
# 876.4K
# Acceptance Rate
# 54.3%
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res,not_pair = 0, False
        s_dict={x:s.count(x) for x in [x for x in set(''.join(s))]}
        for val in s_dict.values():
            if val % 2 == 1:
                res += val-1
                not_pair = True              
            else:
                res += val
        return res if not not_pair else res + 1
    
    
list_s = "abccccdd" ,"a"
for i in list_s:
    Solution.longestPalindrome('Success', i)