
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

 

# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.

# Accepted
# 1.9M
# Submissions
# 4.3M
# Acceptance Rate
# 44.5%

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum, str(s))).lower() # Удаляем все не-алфанумерические символы из строки и приводим к нижнему регистру
        return s == s[::-1] # Возвращаем полученную строку если является палиндромом

list_s = "A man, a plan, a canal: Panama","race a car", " "
for i in list_s:
  Solution.isPalindrome('Success', i)
