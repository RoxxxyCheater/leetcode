
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

#     For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

# Constraints:

#     0 <= x <= 231 - 1

# Accepted
# 1.4M
# Submissions
# 3.9M
# Acceptance Rate
# 37.5%

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        guess = x // 2
        while abs(guess * guess - x) > 1e-6:
            guess = (guess + x / guess) / 2
        return int(guess)        





        # left, right = 0, x  # задаем начальные границы для бинарного поиска
        # while left <= right:  # запускаем бинарный поиск
        #     mid = (left + right) // 2  # находим середину отрезка

        #     if mid * mid <= x < (mid + 1) * (mid + 1):  # если нашли корень, возвращаем его
        #         return mid
        #     elif x < mid * mid:  # если корень больше середины, идем в левую часть
        #         right = mid - 1
        #     else:  # если корень меньше середины, идем в правую часть
        #         left = mid + 1
        # return -1  # если корень не найден, возвращаем -1
    
list_x = 4,8
for i in list_x:
 Solution.mySqrt('Success', i)
