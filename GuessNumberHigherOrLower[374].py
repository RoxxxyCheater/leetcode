# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

 

# Example 1:

# Input: n = 10, pick = 6
# Output: 6
# Example 2:

# Input: n = 1, pick = 1
# Output: 1
# Example 3:

# Input: n = 2, pick = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 231 - 1
# 1 <= pick <= n


# # The guess API is already defined for you.
# # @param num, your guess
# # @return -1 if num is higher than the picked number
# #          1 if num is lower than the picked number
# #          otherwise return 0
# # def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n  # Задаем начальные значения левой и правой границ поиска.
        while left <= right:  # Запускаем цикл, пока левая граница не превышает или равна правой.
            mid = left + (right - left) // 2  # Находим середину текущего диапазона.
            result = guess(mid)  # Вызываем API, чтобы проверить предположение.
            if result == 0:  # Если результат равен 0, это означает, что мы угадали число.
                return mid  # Возвращаем найденное число.
            elif result == -1:  # Если результат равен -1, число меньше нашего предположения.
                right = mid - 1  # Сужаем диапазон поиска, отбрасывая правую часть.
            else:  # Иначе результат равен 1, число больше нашего предположения.
                left = mid + 1  # Сужаем диапазон поиска, отбрасывая левую часть.
    # Замените эту реализацию на фактический вызов API.
    def guess(num):
        # Пример реализации для ориентира, замените его на фактический вызов API.
        pick = 6  # В этом примере выбранное число - 6.
        if num < pick:
            return 1
        elif num > pick:
            return -1
        else:
            return 0



list_n = 10, 1, 2
for i in list_n:
   Solution.guessNumber("Success", i)
