# 171. ExcelSheetColumnNumber
# Easy

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

 

# Example 1:

# Input: columnTitle = "A"
# Output: 1

# Example 2:

# Input: columnTitle = "AB"
# Output: 28

# Example 3:

# Input: columnTitle = "ZY"
# Output: 701

 

# Constraints:

#     1 <= columnTitle.length <= 7
#     columnTitle consists only of uppercase English letters.
#     columnTitle is in the range ["A", "FXSHRXW"].

# Accepted
# 605,298
# Submissions
# 970,958




class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        n = len(columnTitle)
        for i in range(n):
            value = ord(columnTitle[i]) - ord('A') + 1
            result += value * (26 ** (n - i - 1))
        return result
     
     
     
list_wd = "A", "AB", "ZY"
for i in list_wd:
  Solution.titleToNumber('success', i)
