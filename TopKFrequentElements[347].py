#  347. Top K Frequent Elements
# Medium

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

 

# Constraints:

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.

 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# Accepted
# 1,795,480
# Submissions
# 2,856,147


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Подсчитываем частоту каждого элемента в массиве
        counter = Counter(nums)
    
        # Создаем мин-кучу, преобразуя частоту в отрицательное число (так как heapq поддерживает только мин-кучу)
        heap = [(-freq, num) for num, freq in counter.items()]
        # Преобразуем список в кучу
        heapq.heapify(heap)  
    
        result = []
        for _ in range(k):
            # Извлекаем элемент с наивысшей частотой
            freq, num = heapq.heappop(heap)  
            # Добавляем элемент в результирующий список
            result.append(num)  
    
        return result
     
list_n = [1,1,1,2,2,3], [1]
list_ nn = 2, 1

for index, n in enumerate(list_n):
    Solution.topKFrequent('Success', n, list_nn[index])
