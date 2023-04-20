
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Accepted
# 2.1M
# Submissions
# 3.3M
# Acceptance Rate
# 63.1%

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
    if len(s) != len(t):# Отсекаем,если длины строк не равны
        return False
    s_dict = {} # Создаем словарь для частот каждого символа в строке s
    t_dict = {} # Создаем словарь для частот каждого символа в строке t

    for char in s: # Используем метод get для увеличения счетчика символа
        s_dict[char] = s_dict.get(char, 0) + 1
    for char in t: # Используем метод get для увеличения счетчика символа
        t_dict[char] = t_dict.get(char, 0) + 1

   
    return s_dict == t_dict  #Возвращаем True если словари прошли проверку на анаграмму сравнением
       
list_s = "anagram","rat"
list_t = "nagaram","car"
 
for index, num in enumerate(list_s):
    Solution.isAnagram('Success', num, list_t[index])
