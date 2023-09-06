# 1658. Minimum Operations to Reduce X to Zero
# Medium

# 4145

# 81

# Add to List

# Share
# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109
# Accepted
# 113,939
# Submissions
# 302,985

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # Вычисляем общую сумму всех элементов массива.
        total_sum = sum(nums)
        # Вычисляем цель: разницу между суммой всех элементов и x.
        target = total_sum - x
    
        # Если цель равна 0, то мы можем удалить все элементы массива,
        # поэтому возвращаем длину массива.
        if target == 0:
            return len(nums)
    
        # Инициализируем левый указатель для скользящего окна.
        left = 0
        # Инициализируем текущую сумму элементов в скользящем окне.
        curr_sum = 0
        # Инициализируем максимальную длину подмассива с суммой, равной цели.
        max_length = -1
    
        # Проходим по массиву с использованием правого указателя.
        for right in range(len(nums)):
            # Добавляем текущий элемент к текущей сумме.
            curr_sum += nums[right]
    
            # Пока текущая сумма больше цели и левый указатель не превышает правый,
            # убираем элементы с левого конца скользящего окна.
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1
    
            # Если текущая сумма равна цели, обновляем максимальную длину подмассива.
            if curr_sum == target:
                max_length = max(max_length, right - left + 1)
    
        # Если не было найдено подмассива с суммой, равной цели, возвращаем -1.
        if max_length == -1:
            return -1
    
        # Возвращаем минимальное количество операций, необходимых для уменьшения x до 0.
        return len(nums) - max_length



list_nums = [1,1,4,2,3], [5,6,7,8,9], [3,2,20,1,1,3],
list_keys = 10, 4, 5
 
for index, num in enumerate(list_nums):
    Solution.minOperations('Success', num, list_keys[index])
