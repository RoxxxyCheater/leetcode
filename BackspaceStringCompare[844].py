# 844. Backspace String Compare
# Easy

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

 

# Constraints:

#     1 <= s.length, t.length <= 200
#     s and t only contain lowercase letters and '#' characters.

 

# Follow up: Can you solve it in O(n) time and O(1) space?
# Accepted
# 774,670
# Submissions
# 1,578,452




class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Вспомогательная функция для имитации процесса ввода текста
        def build_string(input_str):
            result = []
            for char in input_str:
                if char == '#':
                    # Если встречен символ '#', удаляем последний символ, если результат не пуст
                    if result:
                        result.pop()
                else:
                    # Добавляем символы, отличные от '#', в результат
                    result.append(char)
            return ''.join(result)

        # Сравниваем полученные строки после применения операций удаления
        return build_string(s) == build_string(t)

        return build_string(s) == build_string(t)



l_s = "ab#c", "ab##", "a#c"
l_t =  "ad#c","c#d#", "b"

for t, s in enumerate(l_s):
   Solution.backspaceCompare('Success', s, l_t[t])
