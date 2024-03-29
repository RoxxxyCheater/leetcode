# 2520. Count the Digits That Divide a Number
# Easy

# 457

# 28

# Add to List

# Share
# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.

 

# Example 1:

# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.
# Example 2:

# Input: num = 121
# Output: 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
# Example 3:

# Input: num = 1248
# Output: 4
# Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
 

# Constraints:

# 1 <= num <= 109
# num does not contain 0 as one of its digits.
# Accepted
# 66,376
# Submissions
# 79,151

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0  # Инициализируем счетчик

        # Преобразуем число в строку для итерации по его цифрам
        for digit_str in str(num):
            digit = int(digit_str)

            # Проверяем, делится ли число num на текущую цифру
            if digit != 0 and num % digit == 0:
                count += 1  # Увеличиваем счетчик

        return count


l_n = 7, 121, 1248

for n in l_n:
  Solution.countDigits('Success', n)
