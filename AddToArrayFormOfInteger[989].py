import reduce
# The array-form of an integer num is an array representing its digits in left to right order.

#     For example, for num = 1321, the array form is [1,3,2,1].

# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

# Example 1:

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234

# Example 2:

# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455

# Example 3:

# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        # объединяем числа в списке в одно число, преобразуя каждый элемент в строку и объединяя их методом join добавляя число k
        res = reduce(lambda x, y: x * 10 + y, num) + k
        # возвращаем результат в виде списка цифр числа, преобразовав его в строку и разделив на цифры с помощью map(int, ...)
        return [int(a) for a in str(res)]

list_nums,list_keys = [1,2,0,0],[2,7,4],[2,1,5],34,181,806
 
for index, num in enumerate(list_nums):
    Solution.addToArrayForm('Success', num, list_keys[index])
