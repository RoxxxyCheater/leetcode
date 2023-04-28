# You are given an array of equal-length strings words. Assume that the length of each string is n.

# Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

# For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
# All the strings in words have the same difference integer array, except one. You should find that string.

# Return the string in words that has different difference integer array.

 

# Example 1:

# Input: words = ["adc","wzy","abc"]
# Output: "abc"
# Explanation: 
# - The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
# - The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
# - The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
# The odd array out is [1, 1], so we return the corresponding string, "abc".
# Example 2:

# Input: words = ["aaa","bob","ccc","ddd"]
# Output: "bob"
# Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].
 

# Constraints:

# 3 <= words.length <= 100
# n == words[i].length
# 2 <= n <= 20
# words[i] consists of lowercase English letters.
# Accepted
# 20.8K
# Submissions
# 34.9K
# Acceptance Rate
# 59.6%



class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words[0]) # Получаем длину первого слова
        diff_dict = {} # Словарь разности между символами
        for i in range(n - 1): # Проходимся по всем индексам и словам
            for word in words: 
                diff = ord(word[i+1]) - ord(word[i]) # Находим разность между символами на текущем и следующем индексах
                if i in diff_dict: # Если индекс уже есть в словаре и разность не совпадает, значит это отличающееся слово
                    if diff_dict[i] != diff:
                        return word
                else: # Иначе добавляем разность в словарь для этого индекса
                    diff_dict[i] = diff
    
words_list = ["adc","wzy","abc"], ["aaa","bob","ccc","ddd"]

for i in words_list:
   Solution.oddString('Success', i)



