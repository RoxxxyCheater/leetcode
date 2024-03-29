# 392. Is Subsequence
# Easy

# 7731

# 429

# Add to List

# Share
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
# Accepted
# 899,708
# Submissions
# 1,900,740
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0  # Инициализируем указатели i и j
        m, n = len(s), len(t)  # Получаем длины строк s и t
        
        while i < m and j < n:  # Пока не достигнут конец s или t
            if s[i] == t[j]:  # Если текущие символы совпадают
                i += 1  # Переходим к следующему символу в s
            j += 1  # Переходим к следующему символу в t
        
        return i == m  # Возвращаем True, если все символы s были найдены, иначе False

list_s = "abc",  "axc"
list_t = "ahbgdc", "ahbgdc"
for index, s in enumerate(list_s):
   Solution.isSubsequence('Success', s, list_t[index])
