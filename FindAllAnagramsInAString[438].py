# 438. Find All Anagrams in a String
# Medium

# 12035

# 331

# Add to List

# Share
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.
# Accepted
# 831,525
# Submissions
# 1,641,642


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Инициализация словаря для хранения частот символов в строке p
        char_freq_p = {}
        for char in p:
            char_freq_p[char] = char_freq_p.get(char, 0) + 1

        # Инициализация словаря для хранения частот символов в текущем окне строки s
        char_freq_window = {}
        
        # Инициализация списка для хранения индексов начала анаграмм в строке s
        result = []
        
        # Итерация по строке s
        for i in range(len(s)):
            # Обновление частоты символов в текущем окне строки s
            char_freq_window[s[i]] = char_freq_window.get(s[i], 0) + 1
            
            # Если размер окна превышает длину строки p, удаляем первый символ из окна
            if i >= len(p):
                if char_freq_window[s[i - len(p)]] == 1:
                    del char_freq_window[s[i - len(p)]]
                else:
                    char_freq_window[s[i - len(p)]] -= 1
            
            # Проверка, является ли текущее окно анаграммой строки p
            if char_freq_window == char_freq_p:
                result.append(i - len(p) + 1)

        return result

l_s = "cbaebabacd", "abab"
l_p = "abc", "ab"

for p, s in enumerate(l_s):
    Solution.findAnagrams('Success', s, l_p[p])
