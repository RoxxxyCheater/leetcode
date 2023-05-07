#The Tribonacci sequence Tn is defined as follows: 

#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

#Given n, return the value of Tn.

 

#Example 1:

#Input: n = 4
#Output: 4
#Explanation:
#T_3 = 0 + 1 + 1 = 2
#T_4 = 1 + 1 + 2 = 4
#Example 2:

#Input: n = 25
#Output: 1389537
 

#Constraints:

#0 <= n <= 37
#The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: # если n равно 0, то возвращаем 0
             return 0
        elif n in (1, 2): # если n равно 1 или 2, то возвращаем 1
             return 1
        a, b, c = 0, 1, 1 # инициализация переменных a, b и c
        for _ in range(n-2): # цикл от 0 до n-2
             a, b, c = b, c, a+b+c # переопределение значений переменных a, b и c
        return c # возвращаем значение переменной c


list_n = 4,25

for i in list_n:
    Solution.tribonacci("Success", i)

