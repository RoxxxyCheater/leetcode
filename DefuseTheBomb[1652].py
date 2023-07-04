# 1652. Defuse the Bomb
# Easy

# 646

# 60

# Add to List

# Share
# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

# Example 1:

# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
# Example 2:

# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0. 
# Example 3:

# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
 

# Constraints:

# n == code.length
# 1 <= n <= 100
# 1 <= code[i] <= 100
# -(n - 1) <= k <= n - 1
# Accepted
# 32,378
# Submissions
# 51,809


class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        decrypted = []  # Список для хранения расшифрованного кода
        n = len(code)  # Длина массива code

        if k > 0:  # Если k положительное число, выполняем следующий блок кода
            for i in range(n):  # Проходим по каждому индексу в массиве code
                s = 0  # Инициализируем переменную s для хранения суммы следующих k чисел
                for j in range(1, k + 1):  # Проходим по следующим k числам
                    s += code[(i + j) % n]  # Суммируем следующие k чисел, используя операцию остатка от деления для обеспечения кругового индексирования
                decrypted.append(s)  # Добавляем сумму в расшифрованный код
        elif k < 0:  # Если k отрицательное число, выполняем следующий блок кода
            for i in range(n):  # Проходим по каждому индексу в массиве code
                s = 0  # Инициализируем переменную s для хранения суммы предыдущих abs(k) чисел
                for j in range(1, abs(k) + 1):  # Проходим по предыдущим abs(k) числам
                    s += code[(i - j) % n]  # Суммируем предыдущие abs(k) чисел, используя операцию остатка от деления для обеспечения кругового индексирования
                decrypted.append(s)  # Добавляем сумму в расшифрованный код
        else:  # Если k равно нулю, выполняем следующий блок кода
            decrypted = [0] * n  # Создаем список длины n, заполненный нулями, чтобы расшифрованный код содержал только нули

        return decrypted  # Возвращаем расшифрованный код

list_c = [5,7,1,4], [1,2,3,4],[2,4,9,3]
list_k = 3, 0, -2
for index, c in list_c:
   Solution.decrypt('Success', c, list_k[index])
