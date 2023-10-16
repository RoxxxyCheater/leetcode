# 1832. Check if the Sentence Is Pangram
# Easy

# 2571

# 50

# Add to List

# Share
# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false
 

# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
# Accepted
# 271,609
# Submissions
# 326,856

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # Создаем множество для хранения уникальных букв в предложении
        seen_letters = set()
    
        # Итерируемся по символам в предложении
        for char in sentence:
            if char.isalpha():  # Проверяем, является ли символ буквой английского алфавита
                seen_letters.add(char)  # Добавляем уникальные буквы в множество
    
        # Проверяем, содержит ли множество все 26 букв английского алфавита
        return len(seen_letters) == 26



list_s = "thequickbrownfoxjumpsoverthelazydog", "leetcode"
for i in list_s:
   Solution.checkIfPangram('Success', i)
