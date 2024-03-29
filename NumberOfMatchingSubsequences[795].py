# 792. Number of Matching Subsequences
# Medium

# 5334

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
# 219,673
# Submissions
# 428,515


class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # Вспомогательная функция, которая проверяет, является ли `word` подпоследовательностью строки `s`.
        def isSubsequence(word, s):
            i, j = 0, 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1  # Увеличиваем индекс в `word`, если символы совпадают
                j += 1  # Увеличиваем индекс в строке `s`

            return i == len(word)  # Если `i` становится равным длине `word`, это означает, что `word` является подпоследовательностью `s`

        count = 0  # Инициализируем счетчик
        for word in words:
            # Проверяем, является ли `word` подпоследовательностью `s`
            if isSubsequence(word, s):
                count += 1  # Если является, увеличиваем счетчик
        return count  # Возвращаем общее количество подпоследовательностей


list_s =  "abcde", "dsahjpjauf"
list_w = ["a","bb","acd","ace"], ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
for index, s in enumerate(list_s):
   Solution.numMatchingSubseq('Success', s, list_[index])
