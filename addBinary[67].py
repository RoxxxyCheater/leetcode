# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

 

# Constraints:

#     1 <= a.length, b.length <= 104
#     a and b consist only of '0' or '1' characters.
#     Each string does not contain leading zeros except for the zero itself.

# Accepted
# 1.1M
# Submissions
# 2.1M
# Acceptance Rate
# 52.3%

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a, 2)
        y = int(b, 2)
        return format(x+y, 'b')

list_nums = 11,1010
list_keys = 1,1011

for index, num in enumerate(list_nums):
    Solution.addToArrayForm('Success', num, list_keys[index])