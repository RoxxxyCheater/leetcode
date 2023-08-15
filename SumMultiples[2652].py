# 2652. Sum Multiples
# Easy

# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

 

# Example 1:

# Input: n = 7
# Output: 21
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.

# Example 2:

# Input: n = 10
# Output: 40
# Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.

# Example 3:

# Input: n = 9
# Output: 30
# Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.

 

# Constraints:

#     1 <= n <= 103

# Accepted
# 61,007
# Submissions
# 71,677



class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Инициализация переменной для хранения общей суммы
        total_sum = 0
        
        # Проход по всем числам в диапазоне [1, n]
        for num in range(1, n + 1):
            # Проверка, делится ли текущее число на 3, 5 или 7
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                # Если да, добавляем текущее число к общей сумме
                total_sum += num
        
        # Возвращаем общую сумму чисел, удовлетворяющих условию
        return total_sum


list_n = 7, 10, 9
for i in list_n:
  Solution.sumOfMultiples('Success', i)
