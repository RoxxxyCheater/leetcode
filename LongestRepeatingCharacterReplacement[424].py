# 424. Longest Repeating Character Replacement
# Medium

# 10048

# 461

# Add to List

# Share
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# Accepted
# 640,936
# Submissions
# 1,202,625


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0  # Максимальная длина подстроки с одинаковыми буквами
        max_count = 0  # Максимальное количество одинаковых букв в текущем окне
        char_count = {}  # Словарь для хранения количества встреченных букв

        left = 0  # Левая граница текущего окна

        for right in range(len(s)):  # Проходим по строке
            char_count[s[right]] = char_count.get(s[right], 0) + 1  # Обновляем количество встреченных букв

            max_count = max(max_count, char_count[s[right]])  # Обновляем максимальное количество одинаковых букв в текущем окне

            # Если суммарное количество букв в текущем окне минус максимальное количество одинаковых букв больше k,
            # сдвигаем левую границу окна
            if right - left + 1 - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)  # Обновляем максимальную длину подстроки с одинаковыми буквами

        return max_length  # Возвращаем максимальную длину подстроки с одинаковыми буквами



ls = "ABAB", "AABABBA"
lk = 2, 1

for i, s in enumerate(ls):
    Solution.characterReplacement("Success", s, lk[i])
