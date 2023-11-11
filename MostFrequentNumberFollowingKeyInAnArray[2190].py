# 2190. Most Frequent Number Following Key In an Array
# Easy

# You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

# For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:

#     0 <= i <= nums.length - 2,
#     nums[i] == key and,
#     nums[i + 1] == target.

# Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.

 

# Example 1:

# Input: nums = [1,100,200,1,100], key = 1
# Output: 100
# Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
# No other integers follow an occurrence of key, so we return 100.

# Example 2:

# Input: nums = [2,2,2,2,3], key = 2
# Output: 2
# Explanation: For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key.
# For target = 3, there is only one occurrence at index 4 which follows an occurrence of key.
# target = 2 has the maximum number of occurrences following an occurrence of key, so we return 2.

 

# Constraints:

#     2 <= nums.length <= 1000
#     1 <= nums[i] <= 1000
#     The test cases will be generated such that the answer is unique.

# Accepted
# 31,117
# Submissions
# 52,626



class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        # Создаем пустой словарь для хранения количества встреченных чисел, следующих за ключевым числом
        target_count = {}
    
        # Проходим по списку чисел, исключая последний элемент
        for i in range(len(nums) - 1):
            # Проверяем, является ли текущий элемент числом, равным ключевому числу
            if nums[i] == key:
                # Получаем следующее число (цель) в последовательности
                target = nums[i + 1]
                # Обновляем счетчик для текущей цели в словаре
                target_count[target] = target_count.get(target, 0) + 1
    
        # Находим цель с максимальным количеством, используя функцию max с пользовательским ключом
        max_target = max(target_count, key=target_count.get)
    
        # Возвращаем цель с максимальным количеством
        return max_target


list_n = [1,100,200,1,100], [2,2,2,2,3]
list_k = 1, 2
for index, n in enumerate(list_n):
   Solution.mostFrequent('Success', n, list_k[index])
