# 1780. Check if Number is a Sum of Powers of Three
# Medium

# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.

 

# Example 1:

# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32

# Example 2:

# Input: n = 91
# Output: true
# Explanation: 91 = 30 + 32 + 34

# Example 3:

# Input: n = 21
# Output: false

 

# Constraints:

#     1 <= n <= 107

# Accepted
# 39,260
# Submissions
# 58,414




class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Проверка, может ли число n быть представлено в виде суммы различных степеней тройки
        while n > 0:
            # Проверяем остаток от деления n на 3
            if n % 3 == 2:
                # Если остаток равен 2, то число n не может быть представлено в виде суммы различных степеней тройки
                return False
            # Делим n на 3
            n //= 3
        # Если n становится равным 0, это означает, что n может быть представлено в виде суммы различных степеней тройки
        return True

ln = 12, 91, 21

for i in ln:
   Solution.checkPowersOfThree(´Success´, i)
