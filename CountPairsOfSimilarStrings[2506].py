# 2506. Count Pairs Of Similar Strings
# Easy

# You are given a 0-indexed string array words.

# Two strings are similar if they consist of the same characters.

#     For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
#     However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.

# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

 

# Example 1:

# Input: words = ["aba","aabb","abcd","bac","aabc"]
# Output: 2
# Explanation: There are 2 pairs that satisfy the conditions:
# - i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
# - i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 

# Example 2:

# Input: words = ["aabb","ab","ba"]
# Output: 3
# Explanation: There are 3 pairs that satisfy the conditions:
# - i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
# - i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
# - i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.

# Example 3:

# Input: words = ["nba","cba","dba"]
# Output: 0
# Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.

 

# Constraints:

#     1 <= words.length <= 100
#     1 <= words[i].length <= 100
#     words[i] consist of only lowercase English letters.

# Accepted
# 35,780
# Submissions
# 51,720

class Solution:
    def are_similar(self, word1, word2):
        # Функция для проверки схожести двух слов
        return set(word1) == set(word2)

    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        similar_pairs = set()

        # Перебираем все пары слов
        for i in range(n):
            for j in range(i + 1, n):
                if self.are_similar(words[i], words[j]):
                    # Добавляем пару в множество схожих пар
                    similar_pairs.add((i, j))

        return len(similar_pairs)


words = ["aba","aabb","abcd","bac","aabc"], ["aabb","ab","ba"]

for w in words:
   Solution.similarPairs('Success', w)
