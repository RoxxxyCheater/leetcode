# 869. Reordered Power of 2
# Medium

# 2070

# 425

# Add to List

# Share
# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.

 

# Example 1:

# Input: n = 1
# Output: true
# Example 2:

# Input: n = 10
# Output: false
 

# Constraints:

# 1 <= n <= 109
# Accepted
# 109,023
# Submissions
# 172,617


class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def count_digits(num):
            return sorted(str(num))  # Преобразование числа в строку и сортировка его цифр
        
        power_of_two = 1  # Начинаем с 2^0, то есть 1
        # Пока длина строки, представляющей текущую степень двойки, меньше или равна длине строки n
        while len(str(power_of_two)) <= len(str(n)):
            # Если отсортированные цифры текущей степени двойки совпадают с цифрами n
            if count_digits(power_of_two) == count_digits(n):
                return True  # Возвращаем True, так как найдено совпадение
            power_of_two *= 2  # Увеличиваем степень двойки
        
        return False  # Если не найдено совпадение, возвращаем False

list_n = 1, 10
for i in list_n:
   Solution.reorderedPowerOf2('Success', i)
