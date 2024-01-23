# 1446. Consecutive Characters
# Easy

# 1699

# 33

# Add to List

# Share
# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.
# Accepted
# 157,508
# Submissions
# 260,377


class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 1  # Инициализация максимальной длины (минимально возможной)
    
        current_length = 1  # Инициализация длины текущей последовательной подстроки
        current_char = s[0]  # Инициализация текущего символа
    
        # Итерация по строке, начиная со второго символа
        for i in range(1, len(s)):
            if s[i] == current_char:
                # Если текущий символ такой же, как предыдущий, увеличиваем длину текущей подстроки
                current_length += 1
            else:
                # Если текущий символ отличается, обновляем максимальную длину и сбрасываем текущую длину
                max_length = max(max_length, current_length)
                current_length = 1
                current_char = s[i]
    
        # Обновление максимальной длины после завершения цикла (в случае, если последний символ образует самую длинную последовательную подстроку)
        max_length = max(max_length, current_length)
    
        return max_length

l_s = "leetcode", "abbcccddddeeeeedcba"

for i in l_s:
   Solution.maxPower('Success', i)
