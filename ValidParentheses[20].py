
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
# Accepted
# 3.1M
# Submissions
# 7.7M
# Acceptance Rate
# 40.3%
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # Создание пустого стека для хранения открывающих символов
        pair = {')': '(', '}': '{', ']': '['}  # Словарь, связывающий закрывающие и открывающие символы
        for char in s:  # Проход по каждому символу в строке s
            if char in pair:  # Если символ является закрывающим
                unpair_el = stack.pop() if stack else '#'  # Извлечение последнего элемента из стека или '#' в случае пустого стека
                if pair[char] != unpair_el:  # Если открывающий символ для текущего закрывающего символа не соответствует извлеченному символу
                    return False  # Возвращается False, так как скобки не сбалансированы
            else:  # Если символ является открывающим
                stack.append(char)  # Добавление символа в стек
        return not stack  # Возвращается True, если стек пуст (все скобки сбалансированы), иначе возвращается False

    
list_chars = "()","()[]{}","(]"
for i in list_chars:
   Solution.isValid('Success', i)
