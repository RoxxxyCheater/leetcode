# 2220. Minimum Bit Flips to Convert Number
# Easy

# A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

#     For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.

# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

 

# Example 1:

# Input: start = 10, goal = 7
# Output: 3
# Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
# - Flip the first bit from the right: 1010 -> 1011.
# - Flip the third bit from the right: 1011 -> 1111.
# - Flip the fourth bit from the right: 1111 -> 0111.
# It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

# Example 2:

# Input: start = 3, goal = 4
# Output: 3
# Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
# - Flip the first bit from the right: 011 -> 010.
# - Flip the second bit from the right: 010 -> 000.
# - Flip the third bit from the right: 000 -> 100.
# It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.

 

# Constraints:

#     0 <= start, goal <= 109

# Accepted
# 43,157
# Submissions
# 52,685


class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        flips = 0  # Инициализируем переменную flips для подсчета количества переворотов битов
        while start != goal:  # Пока start и goal не равны друг другу
            if start & 1 != goal & 1:
                # Если текущие биты start и goal не совпадают, требуется перевернуть бит
                flips += 1

            start >>= 1  # Сдвигаем число start вправо на 1 бит
            goal >>= 1  # Сдвигаем число goal вправо на 1 бит

        return flips  # Возвращаем общее количество переворотов битов
    
list_st = 10, 3
list_gl = 7, 4
for index, num in enumerate(list_st):
  Solution.minBitFlips('Success', num, list_gl[index])
