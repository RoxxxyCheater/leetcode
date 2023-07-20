# 412. Fizz Buzz
# Easy

# Given an integer n, return a string array answer (1-indexed) where:

#     answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#     answer[i] == "Fizz" if i is divisible by 3.
#     answer[i] == "Buzz" if i is divisible by 5.
#     answer[i] == i (as a string) if none of the above conditions are true.

 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]

# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

 

# Constraints:

#     1 <= n <= 104

# Accepted
# 1,022,142
# Submissions
# 1,449,459

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []  # Создаем пустой список, в который будем добавлять результаты
        for i in range(1, n + 1):  # Итерируемся от 1 до n включительно
            if i % 3 == 0 and i % 5 == 0:  # Если число делится и на 3, и на 5 без остатка
                result.append("FizzBuzz")  # Добавляем "FizzBuzz" в список результатов
            elif i % 3 == 0:  # Если число делится на 3 без остатка
                result.append("Fizz")  # Добавляем "Fizz" в список результатов
            elif i % 5 == 0:  # Если число делится на 5 без остатка
                result.append("Buzz")  # Добавляем "Buzz" в список результатов
            else:  # Если число не делится ни на 3, ни на 5 без остатка
                result.append(str(i))  # Преобразуем число в строку и добавляем в список результатов
        return result  # Возвращаем список результатов

list_n = 3,5,15
for i in list_n:
   Solution.fizzBuzz('Success', i)
