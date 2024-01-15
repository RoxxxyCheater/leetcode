# 1784. Check if Binary String Has at Most One Segment of Ones
# Easy

# 315

# 929

# Add to List

# Share
# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

# Example 1:

# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
# Example 2:

# Input: s = "110"
# Output: true
 

# Constraints:

# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.
# Accepted
# 39,237
# Submissions
# 99,574


class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_zero = False  # Флаг для отслеживания появления '0' после начала единичного сегмента
    
        for char in s:
            if char == '0':
                seen_zero = True  # Если встречено '0', устанавливаем флаг в True
            elif seen_zero:
                return False  # Если после появления '0' снова встречается '1', значит, есть более одного сегмента единиц
                # Возвращаем False
    
        return True  # Если цикл завершен без встречи '0' после начала сегмента единиц, возвращаем True


 l_s = 1001, 110

for s in l_s:
   Solution.checkOnesSegment('Success', s)
