# 1005. Maximize Sum Of Array After K Negations
# Easy

# Given an integer array nums and an integer k, modify the array in the following way:

#     choose an index i and replace nums[i] with -nums[i].

# You should apply this process exactly k times. You may choose the same index i multiple times.

# Return the largest possible sum of the array after modifying it in this way.

 

# Example 1:

# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose index 1 and nums becomes [4,-2,3].

# Example 2:

# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

# Example 3:

# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

 

# Constraints:

#     1 <= nums.length <= 104
#     -100 <= nums[i] <= 100
#     1 <= k <= 104

# Accepted
# 78,973
# Submissions
# 155,435


class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Сортируем массив в порядке возрастания, чтобы легче было находить наименьшие значения.
        nums.sort()
        
        i = 0
        while k > 0 and i < len(nums) and nums[i] < 0:
            # Негативируем число и уменьшаем k.
            nums[i] = -nums[i]
            k -= 1
            i += 1
        
        # Если остались операции и k все еще больше 0, сортируем массив снова и выполняем их для самого маленького элемента.
        nums.sort()  # Сортируем массив снова
        
        # Если k осталось всё еще больше 0 и является четным, нет необходимости негативировать больше чисел.
        # Если k осталось всё еще больше 0 и является нечетным, негативируем самое маленькое число.
        if k % 2 == 1:
            nums[0] = -nums[0]
        
        # Возвращаем сумму всех элементов в массиве.
        return sum(nums)


list_n = [4,2,3], [3,-1,0,2], [2,-3,-1,5,-4]
list_k = 1, 3, 2

for index, n in enumerate(list_n):
   Solution.largestSumAfterKNegations('Success', n, list_k[index])
