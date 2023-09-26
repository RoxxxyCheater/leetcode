# 917. Reverse Only Letters
# Easy

# 2082

# 66

# Add to List

# Share
# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

 

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
 

# Constraints:

# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
# Accepted
# 181,975
# Submissions
# 288,775


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Преобразуем строку в список символов для возможности изменения
        s = list(s)
        left, right = 0, len(s) - 1
    
        while left < right:
            # Находим первую английскую букву слева
            while left < right and not s[left].isalpha():
                left += 1
    
            # Находим первую английскую букву справа
            while left < right and not s[right].isalpha():
                right -= 1
    
            # Обмениваемся английскими буквами
            s[left], s[right] = s[right], s[left]
    
            left += 1
            right -= 1
    
        # Преобразуем список обратно в строку
        return ''.join(s)

list_s = "ab-cd", "a-bC-dEf-ghIj", "Test1ng-Leet=code-Q!"
for i in list_s:
   Solution.reverseOnlyLetters('Success', i )
