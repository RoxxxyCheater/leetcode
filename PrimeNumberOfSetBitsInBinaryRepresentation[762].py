# 762. Prime Number of Set Bits in Binary Representation
# Easy

# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

# Recall that the number of set bits an integer has is the number of 1's present when written in binary.

#     For example, 21 written in binary is 10101, which has 3 set bits.

 

# Example 1:

# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6  -> 110 (2 set bits, 2 is prime)
# 7  -> 111 (3 set bits, 3 is prime)
# 8  -> 1000 (1 set bit, 1 is not prime)
# 9  -> 1001 (2 set bits, 2 is prime)
# 10 -> 1010 (2 set bits, 2 is prime)
# 4 numbers have a prime number of set bits.

# Example 2:

# Input: left = 10, right = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# 5 numbers have a prime number of set bits.

 

# Constraints:

#     1 <= left <= right <= 106
#     0 <= right - left <= 104

# Accepted
# 93,034
# Submissions
# 134,717


class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Функция для проверки, является ли число простым
        def is_prime(n):
            if n <= 1:  # Числа 0 и 1 не являются простыми
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:  # Если число делится нацело на какое-либо число из интервала [2, квадратный корень из n], то оно не является простым
                    return False
            return True  # Если ни одно из чисел из интервала [2, квадратный корень из n] не делит число n нацело, то оно является простым

        # Функция для подсчета количества установленных битов в двоичном представлении числа
        def count_set_bits(n):
            count = 0
            while n:
                count += n & 1  # Подсчет количества установленных битов
                n >>= 1        # Сдвиг вправо на 1 бит
            return count

        primes = set([2, 3, 5, 7, 11, 13, 17, 19])  # Множество простых чисел до 20

        count = 0
        for num in range(left, right + 1):
            set_bits_count = count_set_bits(num)  # Получение количества установленных битов
            if set_bits_count in primes:          # Проверка, является ли количество простым числом
                count += 1

        return count



ll = 6, 10
lr = 10, 15

for i, l in enumerate(ll):
  Solution.countPrimeSetBits('Success', l, lr[i])
