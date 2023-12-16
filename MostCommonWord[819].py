# 819. Most Common Word
# Easy

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"

 

# Constraints:

#     1 <= paragraph.length <= 1000
#     paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
#     0 <= banned.length <= 100
#     1 <= banned[i].length <= 10
#     banned[i] consists of only lowercase English letters.

# Accepted
# 339,635
# Submissions
# 764,262


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Токенизация слов, игнорируя знаки препинания и приводя к нижнему регистру
        words = re.findall(r'\b\w+\b', paragraph.lower())
    
        # Создание словаря частоты для неблокированных слов
        word_counts = Counter(word for word in words if word not in banned)
    
        # Нахождение самого частого неблокированного слова
        most_common_word = max(word_counts, key=word_counts.get)
    
        return most_common_word

list_p = "Bob hit a ball, the hit BALL flew far after it was hit.",  "a."
list_b = ["hit"], []
for b, p in enumerate(list_p):
  Solution.mostCommonWord('Success', p, list_b[b])
