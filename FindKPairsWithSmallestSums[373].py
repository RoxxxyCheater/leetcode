# 373. Find K Pairs with Smallest Sums
# Medium

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

# Example 3:

# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [[1,3],[2,3]]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

 

# Constraints:

#     1 <= nums1.length, nums2.length <= 105
#     -109 <= nums1[i], nums2[i] <= 109
#     nums1 and nums2 both are sorted in ascending order.
#     1 <= k <= 104

# Accepted
# 243,506
# Submissions
# 606,270


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []    
        heap = [] 
        results = [] 
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j], i, j))    
        push(0, 0) 
        while heap and len(results) < k:
            _, i, j = heapq.heappop(heap)  
            results.append([nums1[i], nums2[j]]) 
            push(i, j + 1)  
            if j == 0:
                push(i + 1, 0)     
        return results
     
list_num1 = [1,7,11], [1,1,2], [1,2]
list_num2 = [2,4,6], [1,2,3], [3]
list_k = 3, 2, 3
for index, num in enumerate(list_num1):
     Solution.totolaCost('Success', num, list_nums2[index], list_k[index])
