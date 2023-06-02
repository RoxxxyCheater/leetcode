# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

 

# Example 1:

# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

# Example 2:

# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".

 

# Constraints:

#     1 <= num.length <= 1000
#     num consists of only digits.
#     num doesn't have any leading zeros.

# Accepted
# 24,164
# Submissions
# 30,474


class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        i = len(num) - 1  # Инициализируем индекс i на последний символ строки num

        while i >= 0 and num[i] == '0':  # Пока индекс i не вышел за границы и текущий символ равен '0'
            i -= 1  # Декрементируем индекс, двигаясь к началу строки

        return num[:i+1]  # Возвращаем подстроку от начала строки до символа с индексом i (включительно)

    
num_list = "51230100","123"
for i in num_list:
   Solution.removeTrailingZeros('Success', i)
 
