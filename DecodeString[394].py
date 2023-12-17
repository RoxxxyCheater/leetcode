# 394. Decode String
# Medium

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

 

# Constraints:

#     1 <= s.length <= 30
#     s consists of lowercase English letters, digits, and square brackets '[]'.
#     s is guaranteed to be a valid input.
#     All the integers in s are in the range [1, 300].

# Accepted
# 732,944
# Submissions
# 1,248,804


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []  # Используем стек для отслеживания состояний (подстрок и их повторений)
        current_num = 0  # Текущее число повторений
        current_str = ''  # Текущая подстрока
    
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Строим число повторений
            elif char.isalpha():
                current_str += char  # Собираем текущую подстроку
            elif char == '[':
                # Начало новой подстроки, сохраняем текущую в стек и сбрасываем состояние
                stack.append((current_str, current_num))
                current_str, current_num = '', 0
            elif char == ']':
                # Обработка завершения повторяющейся подстроки
                prev_str, repeat_count = stack.pop()
                current_str = prev_str + current_str * repeat_count
    
        return current_str


list_s = "3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"

for s in list_s:
   Solution.decodeString('Success', s)
