# 168. Excel Sheet Column Title
# Easy

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

 

# Example 1:

# Input: columnNumber = 1
# Output: "A"

# Example 2:

# Input: columnNumber = 28
# Output: "AB"

# Example 3:

# Input: columnNumber = 701
# Output: "ZY"

 

# Constraints:

#     1 <= columnNumber <= 231 - 1

# Accepted
# 467,399
# Submissions
# 1,190,325



class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        columnTitle = ""  # Инициализируем пустую строку для хранения заголовка столбца

        while columnNumber > 0:  # Запускаем цикл, пока columnNumber больше нуля
            # Вычисляем остаток от деления columnNumber на 26.
            # Этот остаток представляет позицию последнего символа в заголовке столбца.
            remainder = (columnNumber - 1) % 26

            # Добавляем соответствующий символ слева к columnTitle.
            # Для этого используется chr(ord('A') + remainder),
            # чтобы преобразовать остаток в соответствующий символ ASCII ('A' для 0, 'B' для 1 и так далее).
            columnTitle = chr(ord('A') + remainder) + columnTitle

            # Обновляем columnNumber, выполнив целочисленное деление на 26 (целочисленное деление).
            # Это удаляет последний разряд из columnNumber и готовит его к следующей итерации цикла.
            columnNumber = (columnNumber - 1) // 26

        return columnTitle  # Возвращаем получившийся заголовок столбца как результат

list_c =  1, 28, 701
for i in list_c:
  Solution.convertToTitle('Success', i)
