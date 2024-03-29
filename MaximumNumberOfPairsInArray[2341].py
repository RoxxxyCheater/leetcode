# 2341. Maximum Number of Pairs in Array
# Easy

# You are given a 0-indexed integer array nums. In one operation, you may do the following:

#     Choose two integers in nums that are equal.
#     Remove both integers from nums, forming a pair.

# The operation is done on nums as many times as possible.

# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.

 

# Example 1:

# Input: nums = [1,3,2,1,3,2,2]
# Output: [3,1]
# Explanation:
# Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
# Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
# Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
# No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.

# Example 2:

# Input: nums = [1,1]
# Output: [1,0]
# Explanation: Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [].
# No more pairs can be formed. A total of 1 pair has been formed, and there are 0 numbers leftover in nums.

# Example 3:

# Input: nums = [0]
# Output: [0,1]
# Explanation: No pairs can be formed, and there is 1 number leftover in nums.

 

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 100

# Accepted
# 57,730
# Submissions
# 76,480


class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Создаем словарь для подсчета количества вхождений каждого числа в nums
        count_dict = {}
    
        # Итерируемся по элементам в nums и увеличиваем счетчик для каждого числа
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
    
        # Инициализируем переменные для отслеживания количества пар и оставшихся чисел
        pairs = 0
        leftover = 0
    
        # Итерируемся по значениям в словаре (количество вхождений чисел)
        for count in count_dict.values():
            # Рассчитываем количество пар, которые можно сформировать, используя текущее количество
            pairs += count // 2
    
            # Рассчитываем количество оставшихся чисел
            leftover += count % 2
    
        # Возвращаем результат в виде списка [pairs, leftover]
        return [pairs, leftover]

list_n =  [1,3,2,1,3,2,2], [1,1], [0]

for i in list_n:
   Solution.numberOfPairs('Success', i)
