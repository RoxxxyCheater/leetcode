#Given an integer array nums, return the most frequent even element.

#If there is a tie, return the smallest one. If there is no such element, return -1.

 

#Example 1:

#Input: nums = [0,1,2,2,4,4,1]
#Output: 2
#Explanation:
#The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
#We return the smallest one, which is 2.
#Example 2:

#Input: nums = [4,4,4,9,2,4]
#Output: 4
#Explanation: 4 is the even element appears the most.
#Example 3:

#Input: nums = [29,47,21,41,13,37,25,7]
#Output: -1
#Explanation: There is no even element.
 

#Constraints:

#1 <= nums.length <= 2000
#0 <= nums[i] <= 105
#Accepted
#44.3K
#Submissions
#86.6K
#Acceptance Rate
#51.2%

class Solution(object):
    def mostFrequentEven(self, nums):
        freq = {}
        most_frequent = -1
        highest_freq = 0
        
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1
                if freq[num] > highest_freq or (freq[num] == highest_freq and num < most_frequent):
                    highest_freq = freq[num]
                    most_frequent = num
        
        return most_frequent
       
       
       
#         freq = {}
#         for num in nums:
#             if num % 2 == 0:
#                 freq[num] = freq.get(num, 0) + 1
        
#         most_frequent = -1
#         highest_freq = 0
#         for num in freq:
#             if freq[num] > highest_freq or (freq[num] == highest_freq and num < most_frequent):
#                 highest_freq = freq[num]
#                 most_frequent = num
        
#         return most_frequent
  
for i in enumeratelist_nums:
   Solution. mostFrequentEven('Success', i)
