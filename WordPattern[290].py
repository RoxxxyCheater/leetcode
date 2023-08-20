# 290. Word Pattern
# Easy

# 6629

# 817

# Add to List

# Share
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
# Accepted
# 565,454
# Submissions
# 1,356,251


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # Разделяем строку s на слова
        words = s.split()
        
        # Если количество символов в pattern не совпадает с количеством слов в s, возвращаем False
        if len(pattern) != len(words):
            return False
        
        # Создаем два словаря для отображения символов в слова и слов в символы
        char_to_word = {}
        word_to_char = {}
        
        # Проходим по парам символов в pattern и слов в words
        for char, word in zip(pattern, words):
            # Проверяем, есть ли уже отображение для данного символа
            if char in char_to_word:
                # Если отображение уже есть, проверяем, совпадает ли оно с текущим словом
                if char_to_word[char] != word:
                    return False
            else:
                # Если отображения нет, создаем его
                char_to_word[char] = word
            
            # Проверяем, есть ли уже отображение для данного слова
            if word in word_to_char:
                # Если отображение уже есть, проверяем, совпадает ли оно с текущим символом
                if word_to_char[word] != char:
                    return False
            else:
                # Если отображения нет, создаем его
                word_to_char[word] = char
        
        # Если конфликтов не найдено, возвращаем True
        return True

list_g =  "abba", "abba", "aaaa"
list_s = "dog cat cat dog", "dog cat cat fish", "dog cat cat dog"

for index, list_g in enumerate(list_g):
    Solution.wordPattern("Success", list_g, list_s[index])
