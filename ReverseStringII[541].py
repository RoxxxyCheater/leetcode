# 541. Reverse String II
# Easy

# 1790

# 3506

# Add to List

# Share
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104
# Accepted
# 215,850
# Submissions
# 428,319
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []  # Здесь будем хранить окончательный результат
        for i in range(0, len(s), 2 * k):
            # Получаем фрагмент строки размером 2k символов
            chunk = s[i:i + 2 * k]
            # Реверсируем первые k символов внутри фрагмента
            reversed_chunk = chunk[:k][::-1] + chunk[k:]
            result.append(reversed_chunk)
        
        # Объединяем модифицированные фрагменты, чтобы получить окончательный результат
        return ''.join(result)

list_s = "abcdefg", "abcd"
list_k = 2, 2

for index, s in enumerate(list_s):
    Solution.reverseStr("Success", s, list_k[index])
