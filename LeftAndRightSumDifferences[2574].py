# 2574. LeftAndRightSumDifferences
# Easy

# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

#     answer.length == nums.length.
#     answer[i] = |leftSum[i] - rightSum[i]|.

# Where:

#     leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
#     rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

# Return the array answer.

 

# Example 1:

# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

# Example 2:

# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].



# Constraints:

#     1 <= nums.length <= 1000
#     1 <= nums[i] <= 105

# Accepted
# 68,608
# Submissions
# 79,102


class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)  # Получаем длину входного массива
        prefixSum = [0] * (n + 1)  # Инициализируем массив для хранения префиксных сумм
        answer = [0] * n  # Инициализируем массив для хранения абсолютной разницы между суммой слева и суммой справа
        # Вычисляем префиксные суммы для массива nums
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        # Вычисляем абсолютную разницу между суммой слева и суммой справа для каждого индекса
        for i in range(n):
            leftSum = prefixSum[i]  # Сумма элементов слева от индекса i
            rightSum = prefixSum[n] - prefixSum[i + 1]  # Сумма элементов справа от индекса i
            answer[i] = abs(leftSum - rightSum)  # Вычисляем абсолютную разницу
        return answer
        
        # n = len(nums)  # Получаем длину входного массива
        # leftSum = [0] * n  # Инициализируем массив для хранения суммы элементов слева от каждого индекса
        # rightSum = [0] * n  # Инициализируем массив для хранения суммы элементов справа от каждого индекса
        # answer = [0] * n  # Инициализируем массив для хранения абсолютной разницы между суммой слева и суммой справа        
        # for i in range(1, n):# Вычисляем сумму элементов слева для каждого индекса
        #     leftSum[i] = leftSum[i - 1] + nums[i - 1]  # Суммируем предыдущую сумму и элемент слева от текущего индекса           
        # for i in range(n - 2, -1, -1):# Вычисляем сумму элементов справа для каждого индекса
        #     rightSum[i] = rightSum[i + 1] + nums[i + 1]  # Суммируем следующую сумму и элемент справа от текущего индекса            
        # for i in range(n):# Вычисляем абсолютную разницу между суммой слева и суммой справа для каждого индекса
        #     answer[i] = abs(leftSum[i] - rightSum[i])  # Вычисляем абсолютную разницу между суммой слева и суммой справа    
        # return answer

list_n =  [10,4,8,3], [1]
for i in list_n: 
   Solution.leftRightDifference('Success', i)
