# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].

 

# Constraints:

#     0 <= low <= high <= 10^9

# Accepted
# 218K
# Submissions
# 454.5K
# Acceptance Rate
# 48.0%

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        res = high - low +1
        if (res % 2) == 0: return res/2
        else:
            if (high % 2) != 0 or (low % 2) != 0: return int(res/2) +1
            else: return int(res/2)
low_list = 4,9
high_list = 3,7

for index,num in enumerate(low_list):
    Solution.countOdds('Success', low_list[index], high_list[index])