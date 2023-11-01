# 792. Number of Matching Subsequences
# Medium

# 5338

# 226

# Add to List

# Share
# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
# Accepted
# 219,820
# Submissions
# 428,805


class Solution(object):
    def numMatchingSubseq(self, s, words):
        # Функция для проверки, является ли слово подпоследовательностью строки s
        def isSubsequence(word):
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1  # Увеличиваем индекс в слове, если буква совпадает
                i += 1  # Увеличиваем индекс в строке s независимо от совпадения
            return j == len(word)  # Возвращает True, если все буквы word обработаны в s

        count = 0  # Переменная для подсчета количества подпоследовательностей
        for word in words:
            if isSubsequence(word):
                count += 1  # Увеличиваем счетчик, если слово - подпоследовательность

        return count  # Возвращаем общее количество подпоследовательностей

list_s = "abcde", "dsahjpjauf"
list_w = ["a","bb","acd","ace"], ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

for index, s in enumerate(list_s):
   Solution.numMatchingSubseq('Success', s, list_w[index])
