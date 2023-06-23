# 1027. Longest Arithmetic Subsequence
# Medium

# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

# Note that:

#     A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#     A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

 

# Example 1:

# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:  The whole array is an arithmetic sequence with steps of length = 3.

# Example 2:

# Input: nums = [9,4,7,2,10]
# Output: 3
# Explanation:  The longest arithmetic subsequence is [4,7,10].

# Example 3:

# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:  The longest arithmetic subsequence is [20,15,10,5].

 

# Constraints:

#     2 <= nums.length <= 1000
#     0 <= nums[i] <= 500

# Accepted
# 143,808
# Submissions
# 293,005


class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [{} for _ in range(n)]  # Массив для хранения длин арифметических последовательностей        
        max_len = 2  # Максимальная длина арифметической последовательности        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]  # Разность между текущим и предыдущим элементами
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1  # Если разность уже присутствует в предыдущей арифметической последовательности, увеличиваем длину на 1
                else:
                    dp[i][diff] = 2  # Иначе, начинаем новую арифметическую последовательность длиной 2
                max_len = max(max_len, dp[i][diff])  # Обновляем максимальную длину, если необходимо
        return max_len

list_nums = [3,6,9,12],[9,4,7,2,10],[20,1,15,3,10,5,8]
for i in list_nums:
  Solution.longesdtArithSeqLength('Success', i)
