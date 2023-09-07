# 2544. Alternating Digit Sum
# Easy

# 323

# 17

# Add to List

# Share
# You are given a positive integer n. Each digit of n has a sign according to the following rules:

# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.

 

# Example 1:

# Input: n = 521
# Output: 4
# Explanation: (+5) + (-2) + (+1) = 4.
# Example 2:

# Input: n = 111
# Output: 1
# Explanation: (+1) + (-1) + (+1) = 1.
# Example 3:

# Input: n = 886996
# Output: 0
# Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
 

# Constraints:

# 1 <= n <= 109
 

# Accepted
# 43,274
# Submissions
# 63,198


class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Инициализируем общую сумму
        total = 0

        # Преобразуем n в строку для итерации по его цифрам
        n_str = str(n)

        # Инициализируем знак как положительный (так как наиболее значимая цифра всегда положительная)
        sign = 1

        # Итерируемся по цифрам в n_str
        for digit_char in n_str:
            # Преобразуем символ цифры в целое число
            digit = int(digit_char)

            # Добавляем цифру к общей сумме с учетом текущего знака
            total += sign * digit

            # Меняем знак для следующей цифры (противоположный знак)
            sign *= -1

        # Возвращаем общую сумму с учетом знаков
        return total

list_n =  521, 111, 886996
for i in list_n:
  Solution.alternateDigitSum('Success', i)
