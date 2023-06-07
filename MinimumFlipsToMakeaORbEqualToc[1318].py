# Medium

# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

# Example 1:

# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1

# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0

 

# Constraints:

#     1 <= a <= 10^9
#     1 <= b <= 10^9
#     1 <= c <= 10^9

# Accepted
# 82,647
# Submissions
# 115,608


class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        count = 0

        while a or b or c:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 1 and (bit_a == 0 and bit_b == 0):
                count += 1
            elif bit_c == 0:
                if bit_a == 1 and bit_b == 1:
                    count += 2
                elif bit_a == 1 or bit_b == 1:
                    count += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return count
    
list_a = 2, 4, 1
list_b = 6, 2, 2 
list_c = 5, 7, 3

for index, num in enumerate(list_a):
  Solution.minFlips('Success', num, list_b[index], list_c[index])
