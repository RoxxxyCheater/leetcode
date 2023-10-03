# 345. Reverse Vowels of a String
# Easy

# 4031

# 2666

# Add to List

# Share
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.
# Accepted
# 629,317
# Submissions
# 1,225,720

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """       
        s = list(s)
        vowels = "aeiouAEIOU"
        left, right = 0, len(s) - 1
        while left < right
            while left < right and s[left] not in vowels:
                left += 1            
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


list_s = "hello", "leetcode"
for i in list_s:
   Solution.reverseVowels('Success', i)
