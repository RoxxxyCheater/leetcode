# 209. MinimumSizeSubarraySum
# Medium

# 10843

# 298

# Add to List

# Share
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
# Accepted
# 782,319
# Submissions
# 1,689,573


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # Длина массива
        left = 0  # Левый указатель начинает с индекса 0
        subarray_sum = 0  # Инициализируем сумму подмассива нулем
        min_length = float('inf')  # Изначально устанавливаем наименьшую длину в бесконечность
        
        for right in range(n):  # Проходим по массиву с помощью правого указателя
            subarray_sum += nums[right]  # Добавляем текущий элемент к сумме подмассива
            
            while subarray_sum >= target:  # Пока сумма подмассива больше или равна целевому значению
                min_length = min(min_length, right - left + 1)  # Проверяем, является ли текущая длина подмассива наименьшей и обновляем ее
                subarray_sum -= nums[left]  # Уменьшаем сумму подмассива, удаляя левый элемент
                left += 1  # Сдвигаем левый указатель вправо
        
        return min_length if min_length != float('inf') else 0  # Возвращаем наименьшую длину подмассива, если такой подмассив существует, иначе возвращаем 0
        


        # n = len(nums)  # Длина массива
        # left = 0  # Левый указатель начинает с индекса 0
        # subarray_sum = 0  # Инициализируем сумму подмассива нулем
        # min_length = float('inf')  # Изначально устанавливаем наименьшую длину в бесконечность
        
        # for right in range(n):  # Проходим по массиву с помощью правого указателя
        #     subarray_sum += nums[right]  # Добавляем текущий элемент к сумме подмассива
            
        #     while subarray_sum >= target:  # Пока сумма подмассива больше или равна целевому значению
        #         min_length = min(min_length, right - left + 1)  # Проверяем, является ли текущая длина подмассива наименьшей и обновляем ее
        #         subarray_sum -= nums[left]  # Уменьшаем сумму подмассива, удаляя левый элемент
        #         left += 1  # Сдвигаем левый указатель вправо
        
        # return min_length if min_length != float('inf') else 0  # Возвращаем наименьшую длину подмассива, если такой подмассив существует, иначе возвращаем 0

list_t = 7, 4, 11
list_n = [2,3,1,2,4,3], [1,4,4], [1,1,1,1,1,1,1,1]
for index, num in enumerate(list_t):
   Solution.minSubArrayLen('Success', num, list_n[index])
