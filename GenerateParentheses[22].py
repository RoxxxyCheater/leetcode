# 22. Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

 

# Constraints:

#     1 <= n <= 8

# Accepted
# 1,645,759
# Submissions
# 2,228,572



class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []  # Список для хранения всех комбинаций скобок
    
        def backtrack(s='', left=0, right=0):
            """
            Рекурсивная функция для генерации комбинаций скобок.
    
            :param s: текущая строка скобок
            :param left: количество открытых скобок
            :param right: количество закрытых скобок
            """
            # Базовый случай: когда строка достигла нужной длины
            if len(s) == 2 * n:
                result.append(s)
                return
            # Рекурсивные случаи
            if left < n:
                # Добавляем открывающую скобку, если это разрешено
                backtrack(s + '(', left + 1, right)
            if right < left:
                # Добавляем закрывающую скобку, если это разрешено
                backtrack(s + ')', left, right + 1)
    
        # Начинаем рекурсию
        backtrack()
        return result


l_n = 3, 1

for n in l_n:
   Solution.generateParenthesis('Success', n)
