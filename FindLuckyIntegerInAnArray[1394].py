# 1394. Find Lucky Integer in an Array
# Easy

# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

 

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.

 

# Constraints:

#     1 <= arr.length <= 500
#     1 <= arr[i] <= 500

# Accepted
# 100,724
# Submissions
# 154,484
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Создаем словарь для подсчета частоты встречаемости чисел
        freq = {}    
        # Подсчитываем частоту встречаемости каждого числа в массиве
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1    
        # Инициализируем наибольшее счастливое число значением -1
        largest_lucky = -1    
        # Проходим через словарь и находим наибольшее счастливое число
        for num, count in freq.items():
            if num == count and num > largest_lucky:
                largest_lucky = num
        # Возвращаем наибольшее счастливое число
        return largest_lucky


list_a = [2,2,3,4], [1,2,2,3,3,3], [2,2,2,3,3]
for arr in list_a:
   Solution.findLucky('Success', arr)
