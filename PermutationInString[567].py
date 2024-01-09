# 567. Permutation in String
# Medium

# 10959

# 370

# Add to List

# Share
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.
# Accepted
# 780,794
# Submissions
# 1,765,386



class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Проверка, если длина s1 больше длины s2, то перестановки не могут вмещаться.
        if len(s1) > len(s2):
            return False

        # Инициализация размера окна и счетчиков символов в строках.
        window_size = len(s1)
        target_count = Counter(s1)
        current_count = Counter(s2[:window_size])

        # Проверка совпадения для начального окна.
        for i in range(len(s2) - window_size + 1):
            if current_count == target_count:
                return True

            # Обновление счетчика для следующего окна.
            if i + window_size < len(s2):
                # Уменьшение счетчика для символа, который выходит из окна.
                current_count[s2[i]] -= 1
                if current_count[s2[i]] == 0:
                    del current_count[s2[i]]

                # Увеличение счетчика для нового символа в окне.
                current_count[s2[i + window_size]] += 1

        return False


l1 = "ab", "ab"
l2 = "eidbaooo", "eidboaoo"

for s2, s1 in enumerate(l1):
    Solution.checkInclusion('Success', s1, l2[s2])
