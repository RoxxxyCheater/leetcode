# 728. Self Dividing Numbers
# Easy

# 1713

# 368

# Add to List

# Share
# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

# Example 1:

# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:

# Input: left = 47, right = 85
# Output: [48,55,66,77]
 

# Constraints:

# 1 <= left <= right <= 104
# Accepted
# 229,796
# Submissions
# 293,568


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []  # Список для хранения самоделительных чисел
        
        # Проходим по диапазону чисел от left до right включительно
        for num in range(left, right + 1):
            if self.isSelfDividing(num):
                result.append(num)
                
        return result
    
    def isSelfDividing(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Преобразуем число в строку для итерации по его цифрам
        for digit in str(num):
            # Проверяем наличие цифры 0 и деление числа на каждую цифру
            if digit == '0' or num % int(digit) != 0:
                return False
        return True
    
l_l = 1, 47
l_r = 22, 85

for r, l in enumerate(l_l):
    Solution.selfDividingNumbers('Success', l, l_r[r])
