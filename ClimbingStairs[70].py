# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

 

# Constraints:

#     1 <= n <= 45

# Accepted
# 2.2M
# Submissions
# 4.2M
# Acceptance Rate
# 52.2%


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:return n # если n меньше или равно 2, то количество способов равно n
        res, one, two = 0, 1, 2
        for i in range(3, n + 1): # начинаем с 3, так как мы уже рассмотрели случаи для n = 1 и n = 2
            res = one + two # считаем количество способов для i-ой ступеньки как сумму способов для i-2 и i-1 ступенек
            one, two = two, res # обновляем значения one и two для следующей итерации
        return res
       
       
               if n <= 2:  
            return n
        res, one, two = 0, 1, 2
        
        for i in range(3, n + 1):
            
            res = one + two
            # обновляем значения one и two для следующей итерации
            one, two = two, res
        return res

list_nums = 44, 2,3, 99
for i in list_nums:
    print(Solution.climbStairs('Success', i))
