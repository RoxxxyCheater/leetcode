# 2490. Circular Sentence
# Easy

# 277

# 7

# Add to List

# Share
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

# A sentence is circular if:

# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

# Given a string sentence, return true if it is circular. Otherwise, return false.

 

# Example 1:

# Input: sentence = "leetcode exercises sound delightful"
# Output: true
# Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
# - leetcode's last character is equal to exercises's first character.
# - exercises's last character is equal to sound's first character.
# - sound's last character is equal to delightful's first character.
# - delightful's last character is equal to leetcode's first character.
# The sentence is circular.
# Example 2:

# Input: sentence = "eetcode"
# Output: true
# Explanation: The words in sentence are ["eetcode"].
# - eetcode's last character is equal to eetcode's first character.
# The sentence is circular.
# Example 3:

# Input: sentence = "Leetcode is cool"
# Output: false
# Explanation: The words in sentence are ["Leetcode", "is", "cool"].
# - Leetcode's last character is not equal to is's first character.
# The sentence is not circular.
 

# Constraints:

# 1 <= sentence.length <= 500
# sentence consist of only lowercase and uppercase English letters and spaces.
# The words in sentence are separated by a single space.
# There are no leading or trailing spaces.
# Accepted
# 29,738
# Submissions
# 46,926


class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words = sentence.split()  # Разделяем предложение на слова по пробелам и сохраняем их в список
        n = len(words)  # Количество слов в предложении
        
        for i in range(n):
            curr_word = words[i]  # Текущее слово
            next_word = words[(i + 1) % n]  # Следующее слово (при достижении конца списка, переходим к первому слову)
            if curr_word[-1] != next_word[0]:  # Проверяем, равны ли последний символ текущего слова и первый символ следующего слова
                return False  # Если символы не равны, предложение не является круговым
        
        return words[-1][-1] == words[0][0]  # Проверяем, равны ли последний символ последнего слова и первый символ первого слова

list_s = "leetcode exercises sound delightful", "eetcode",  "Leetcode is cool"
for i in list_s:
  Solution. isCircularSentence('Success', i)
