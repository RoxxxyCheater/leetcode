# 228. Summary Ranges

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 

# Constraints:

# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.
# Accepted
# 405,913
# Submissions
# 830,115
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
    
        ranges = []  # Инициализируем пустой список для хранения диапазонов
        start = end = nums[0]  # Инициализируем начальное значение диапазона
    
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                # Если текущий элемент следует за предыдущим элементом,
                # то продолжаем расширять диапазон
                end = nums[i]
            else:
                # Если текущий элемент не следует за предыдущим,
                # то добавляем текущий диапазон в результат и
                # обновляем начальное и конечное значения для нового диапазона
                ranges.append(formatRange(start, end))
                start = end = nums[i]
    
        # Добавляем последний диапазон в результат
        ranges.append(formatRange(start, end))
        return ranges
    
    def formatRange(start, end):
        if start == end:
            # Если начальное и конечное значения равны,
            # возвращаем только один элемент
            return str(start)
        else:
            # Иначе возвращаем диапазон в формате "start->end"
            return str(start) + '->' + str(end)

list_num = [0,1,2,4,5,7],[0,2,3,4,6,8,9]
for i in list_num:
  Solution.summaryRanges('Success', i)
