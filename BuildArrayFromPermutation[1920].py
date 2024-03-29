# 1920. Build Array from Permutation
# Easy

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

 

# Example 1:

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows: 
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]

# Example 2:

# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
#     = [4,5,0,1,2,3]

 

# Constraints:

#     1 <= nums.length <= 1000
#     0 <= nums[i] < nums.length
#     The elements in nums are distinct.

 

# Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?
# Accepted
# 385,959
# Submissions
# 430,639


[4] final v2
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)  # Получаем длину входного массива
        
        # # Создаем массив для хранения результата
        # ans = [0] * n
        
        # # Проходим по каждому индексу i в массиве
        # for i in range(n):
        #     # Заполняем текущий индекс в ans значением по индексу nums[i] в nums
        #     ans[i] = nums[nums[i]]
        
        # return ans  # Возвращаем результирующий массив

   
       n = len(nums)  # Получаем длину входного массива
       
       # Проходим по каждому индексу i в массиве
       for i in range(n):
           # Добавляем в nums[i] новое значение, которое представляет собой
           # перемещение nums[nums[i]] на n позиций влево, чтобы кодировать два значения
           nums[i] += n * (nums[nums[i]] % n)
       
       # После первого прохода, каждый элемент nums[i] содержит два значения:
       # оригинальное значение и новое значение
       
       # Проходим по массиву еще раз, чтобы извлечь новые значения
       for i in range(n):
           nums[i] //= n  # Извлекаем новое значение, выполнив целочисленное деление на n
       
       return nums  # Возвращаем измененный массив nums

list_n = [0,2,1,5,3,4], [5,0,1,2,3,4]
for i in list_n:  
   Solution.buildArray('Success', i)
