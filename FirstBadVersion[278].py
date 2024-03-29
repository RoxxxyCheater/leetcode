    
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1
 

# Constraints:

# 1 <= bad <= n <= 231 - 1
# Accepted
# 1,489,037
# Submissions
# 3,425,488

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
        """
        :type n: int
        :rtype: int
        """
        left = 1  # Начальная версия, с которой начинается поиск
        right = n  # Конечная версия, с которой заканчивается поиск

        while left < right:  # Пока левая граница меньше правой границы
            mid = left + (right - left) // 2  # Вычисляем среднюю версию

            if isBadVersion(mid):  # Если средняя версия плохая
                right = mid  # Сужаем диапазон поиска до версий слева от средней
            else:
                left = mid + 1  # Сужаем диапазон поиска до версий справа от средней

        return left  # Возвращаем значение левой границы как первую плохую версию
    
list_n = 5,1

for index,num in enumerate(list_n):
    Solution.firstBadVersion('Success', num)
