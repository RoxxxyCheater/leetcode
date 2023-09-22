# 1748. Sum of Unique Elements
# Easy

# 1384

# 34

# Add to List

# Share
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

 

# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# Accepted
# 133,358
# Submissions
# 174,001

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Создаем словарь для хранения количества вхождений каждого элемента
        count_dict = {}
        
        # Проходим по массиву и подсчитываем количество вхождений каждого элемента
        for num in nums:
            # Если элемент уже есть в словаре, увеличиваем его счетчик на 1
            if num in count_dict:
                count_dict[num] += 1
            # Если элемента нет в словаре, добавляем его и устанавливаем счетчик в 1
            else:
                count_dict[num] = 1
        
        # Суммируем уникальные элементы (те, у которых количество равно 1)
        unique_sum = 0
        for num, count in count_dict.items():
            # Если счетчик равен 1, значит, элемент уникален, и мы добавляем его к сумме
            if count == 1:
                unique_sum += num
        
        # Возвращаем общую сумму уникальных элементов
        return unique_sum



list_n = [1,2,3,2], [1,1,1,1,1], [1,2,3,4,5]
for i in list_n:
   Solution.sumOfUnique('Success', i)
