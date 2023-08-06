# 372. Super Pow
# Medium

# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

 

# Example 1:

# Input: a = 2, b = [3]
# Output: 8

# Example 2:

# Input: a = 2, b = [1,0]
# Output: 1024

# Example 3:

# Input: a = 1, b = [4,3,3,8,5,2]
# Output: 1

 

# Constraints:

#     1 <= a <= 231 - 1
#     1 <= b.length <= 2000
#     0 <= b[i] <= 9
#     b does not contain leading zeros.

# Accepted
# 62,204
# Submissions
# 173,094

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337
    
        # Helper function to calculate (a^k) % 1337
        def power(a, k):
            result = 1
            a %= MOD
            while k > 0:
                if k % 2 == 1:
                    result = (result * a) % MOD
                k //= 2
                a = (a * a) % MOD
            return result
    
        result = 1
        for digit in b:
            # Update the result for each digit in b
            result = (power(result, 10) * power(a, digit)) % MOD
    
        return result
    
list_a =  2, 2, 1
list_b = [3], [1,0], [4,3,3,8,5,2]

for index, list_a in enumerate(list_a):
    Solution.findContentChildren("Success", list_a, list_b[index])
