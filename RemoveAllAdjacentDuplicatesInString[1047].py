# 1047. Remove All Adjacent Duplicates In String
# Easy

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# Example 2:

# Input: s = "azxxzy"
# Output: "ay"

 

# Constraints:

#     1 <= s.length <= 105
#     s consists of lowercase English letters.

# Accepted
# 513,980
# Submissions
# 743,041


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []  # Используем стек для отслеживания символов
    
        for char in s:
            if stack and stack[-1] == char:
                # Если текущий символ равен вершине стека, удаляем вершину стека (дубликат)
                stack.pop()
            else:
                # Иначе добавляем текущий символ в стек
                stack.append(char)
    
        return ''.join(stack)  # Собираем символы из стека в строку и возвращаем результат

     
l_s = "abbaca", "azxxzy"
for i in l_s:
   Soluiton.removeDuplicates('Success', i)
