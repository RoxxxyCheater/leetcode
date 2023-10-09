# 557. Reverse Words in a String III
# Easy

# 5674

# 240

# Add to List

# Share
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.
# Accepted
# 830,449
# Submissions
# 1,002,168


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Разбиваем предложение на слова
        words = s.split()
    
        # Создаем новый список для хранения перевернутых слов
        reversed_words = [word[::-1] for word in words]
    
        # Объединяем перевернутые слова обратно в предложение с пробелами
        reversed_sentence = " ".join(reversed_words)
    
        return reversed_sentence




list_s = "Let's take LeetCode contest", "God Ding"
for i in list_n:
   Solution. reverseWords('Success', i)
