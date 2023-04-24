
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

 

# Constraints:

#     1 <= ransomNote.length, magazine.length <= 105
#     ransomNote and magazine consist of lowercase English letters.

# Accepted
# 744.4K
# Submissions
# 1.3M
# Acceptance Rate
# 58.3%

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return self
    

ransomNote_list = "a", "aa", "aa"
magazine_list = "b", "ab", "aab"

for index, strs in enumerate(ransomNote_list):
    Solution.canConstruct('Succes',strs, magazine_list[index])