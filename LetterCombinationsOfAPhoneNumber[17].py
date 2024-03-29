# 17. Letter Combinations of a Phone Number
# Medium

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = ""
# Output: []

# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

 

# Constraints:

#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9'].

# Accepted
# 1,854,671
# Submissions
# 3,121,525

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Отображение цифр на соответствующие буквы
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            # Если мы достигли конца строки digits, добавляем текущую комбинацию
            if index == len(digits):
                combinations.append(''.join(path))
                return

            # Получаем буквы, соответствующие текущей цифре
            letters = digit_map[digits[index]]

            # Рекурсивно строим комбинации для следующей цифры
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # Откатываем изменение для следующей итерации

        combinations = []
        backtrack(0, [])
        return combinations

l_d = "23", "", "2"
for d in l_d:
   Solution.letterCombinations('Success', d)
