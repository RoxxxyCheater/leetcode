# 1869. Longer Contiguous Segments of Ones than Zeros
# Easy

# 501

# 13

# Add to List

# Share
# Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

# For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

 

# Example 1:

# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.
# Example 2:

# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.
# Example 3:

# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.
 

# Constraints:

# 1 <= s.length <= 100
# s[i] is either '0' or '1'.
# Accepted
# 44,399
# Submissions
# 73,184


class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Инициализация переменных для хранения максимальной длины сегментов
        max_ones_length = 0  # Максимальная длина сегмента единиц
        max_zeros_length = 0  # Максимальная длина сегмента нулей
    
        # Инициализация переменных для текущей длины сегментов
        current_ones_length = 0  # Текущая длина сегмента единиц
        current_zeros_length = 0  # Текущая длина сегмента нулей
    
        # Итерация по символам бинарной строки
        for char in s:
            if char == '1':
                # Если встречена '1', увеличиваем текущую длину сегмента единиц
                current_ones_length += 1
                # Обнуляем текущую длину сегмента нулей
                current_zeros_length = 0
            elif char == '0':
                # Если встречен '0', увеличиваем текущую длину сегмента нулей
                current_zeros_length += 1
                # Обнуляем текущую длину сегмента единиц
                current_ones_length = 0
    
            # Обновление максимальных длин сегментов
            max_ones_length = max(max_ones_length, current_ones_length)
            max_zeros_length = max(max_zeros_length, current_zeros_length)
    
        # Сравнение максимальных длин сегментов и возвращение результата
        return max_ones_length > max_zeros_length



l_s = "1101", "11100", "110100010"

for s in l_s:
   Solution.checkZeroOnes('Success', s)
