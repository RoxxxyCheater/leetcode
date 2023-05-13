# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".

# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.

 

# Constraints:

#     1 <= words.length <= 100
#     1 <= words[i].length <= 30
#     words[i] contains only lowercase English letters.
#     All the strings of words are unique.

# Accepted
# 70,544
# Submissions
# 110,714
# Seen this question in a real interview before?


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return words
    
    
list_num = ["mass","as","hero","superhero"], ["leetcode","et","code"],["blue","green","bu"]
for i in list_num:
    Solution.stringMatching('Success', i)