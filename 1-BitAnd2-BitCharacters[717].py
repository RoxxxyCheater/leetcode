# 717. 1-bit and 2-bit Characters
# Easy

# 850

# 2067

# Add to List

# Share
# We have two special characters:

# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

# Example 1:

# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
# Example 2:

# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.
 

# Constraints:

# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.
# Accepted
# 127,673
# Submissions
# 282,820


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        i = 0

        # Итеративный процесс по проверке каждого бита
        while i < n - 1:
            # Если текущий бит - 1, значит, следующий бит тоже двубитный символ, переходим через два бита
            if bits[i] == 1:
                i += 2
            # Если текущий бит - 0, это однобитный символ, переходим через один бит
            else:
                i += 1

        # Если i оказывается равным n - 1, то последний символ обязательно однобитный
        return i == n - 1


l_b = [1,0,0], [1,1,1,0]

for i in l_b:
   Solution.isOneBitCharacter('Success', i)
