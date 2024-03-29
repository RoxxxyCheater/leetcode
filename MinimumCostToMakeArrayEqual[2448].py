# 2448. Minimum Cost to Make Array Equal
# Hard

# 1956

# 25

# Add to List

# Share
# You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

# You can do the following operation any number of times:

# Increase or decrease any element of the array nums by 1.
# The cost of doing one operation on the ith element is cost[i].

# Return the minimum total cost such that all the elements of the array nums become equal.

 

# Example 1:

# Input: nums = [1,3,5,2], cost = [2,3,1,14]
# Output: 8
# Explanation: We can make all the elements equal to 2 in the following way:
# - Increase the 0th element one time. The cost is 2.
# - Decrease the 1st element one time. The cost is 3.
# - Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
# The total cost is 2 + 3 + 3 = 8.
# It can be shown that we cannot make the array equal with a smaller cost.
# Example 2:

# Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
# Output: 0
# Explanation: All the elements are already equal, so no operations are needed.
 

# Constraints:

# n == nums.length == cost.length
# 1 <= n <= 105
# 1 <= nums[i], cost[i] <= 106

# Accepted
# 50,477
# Submissions
# 109,714

class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_cost = 0
        n = len(nums)
        
        # Итерируемся по массиву и сравниваем соседние элементы
        i = 1
        while i < n:
            # Если текущий элемент равен предыдущему, считаем стоимость изменения
            if nums[i] == nums[i - 1]:
                total_cost += min(cost[i], cost[i - 1])  # Добавляем минимальную стоимость изменения
                max_cost = max(cost[i], cost[i - 1])  # Находим максимальную стоимость изменения
                j = i + 1
                
                # Находим группу с одинаковыми числами и суммируем их стоимость
                while j < n and nums[j] == nums[i]:
                    total_cost += min(max_cost, cost[j])  # Добавляем минимальную стоимость изменения
                    max_cost = max(max_cost, cost[j])  # Обновляем максимальную стоимость изменения
                    j += 1
                    
                i = j  # Переходим к следующей группе
            else:
                i += 1
        
        return total_cost

list_num = [1,3,5,2], [2,2,2,2,2]
list_cost = [2,3,1,14], [4,2,8,1,3]

for index, num in enumerate(list_num):
   Solution.minCost('Success', num, list_cost[index])
