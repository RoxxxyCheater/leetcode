# 1995. Count Special Quadruplets
# Easy

# 574

# 215

# Add to List

# Share
# Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

# nums[a] + nums[b] + nums[c] == nums[d], and
# a < b < c < d
 

# Example 1:

# Input: nums = [1,2,3,6]
# Output: 1
# Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
# Example 2:

# Input: nums = [3,3,6,4,5]
# Output: 0
# Explanation: There are no such quadruplets in [3,3,6,4,5].
# Example 3:

# Input: nums = [1,1,1,3,5]
# Output: 4
# Explanation: The 4 quadruplets that satisfy the requirement are:
# - (0, 1, 2, 3): 1 + 1 + 1 == 3
# - (0, 1, 3, 4): 1 + 1 + 3 == 5
# - (0, 2, 3, 4): 1 + 1 + 3 == 5
# - (1, 2, 3, 4): 1 + 1 + 3 == 5
 

# Constraints:

# 4 <= nums.length <= 50
# 1 <= nums[i] <= 100
# Accepted
# 34,783
# Submissions
# 57,770


class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0  # Инициализируем счетчик числа четверок, удовлетворяющих условию
        n = len(nums)  # Получаем длину массива nums
        
        for a in range(n):  # Первый цикл перебирает индекс a от 0 до n-1
            for b in range(a + 1, n):  # Второй цикл перебирает индекс b от a+1 до n-1
                for c in range(b + 1, n):  # Третий цикл перебирает индекс c от b+1 до n-1
                    for d in range(c + 1, n):  # Четвертый цикл перебирает индекс d от c+1 до n-1
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            # Проверяем, удовлетворяет ли сумма элементов в четверке условию
                            count += 1  # Если условие выполняется, увеличиваем счетчик на 1

        return count  # Возвращаем общее количество четверок, удовлетворяющих условию








list_n = [1,2,3,6], [3,3,6,4,5], [1,1,1,3,5]
for i in list_n:
   Solution.countQuadruplets('Success', i)
