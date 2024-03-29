
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
 

# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 
# Accepted
# 184.9K
# Submissions
# 265.5K
# Acceptance Rate
# 69.6%

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row,second_row,third_row,result  = set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm"),[] # три ряда клавиатуры и результат
        for word in words:
            word_set = set(word.lower())  # Преобразуем слово во множество букв в нижнем регистре
            if word_set.issubset(first_row) or word_set.issubset(second_row) or word_set.issubset(third_row): # Если один ряд клавиатуры, добавляем слово
                result.append(word)
        return result
    
words_list = ["Hello","Alaska","Dad","Peace"],["omk"],["adsdf","sfd"]

for i in words_list:
 Solution.findWords('Success', i)
