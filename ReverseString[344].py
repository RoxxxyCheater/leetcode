# 344. Reverse String
# Easy

# 7920

# 1126

# Add to List

# Share
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.
# Accepted
# 2,261,319
# Submissions
# 2,927,123

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1 # Инициализируем два указателя в начале и конце массива
        while left < right:
            # Меняем местами символы, на которые указывают левый и правый указатели
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


list_s = ["h","e","l","l","o"],  ["H","a","n","n","a","h"]

for i in list_s:
   Solution.reverseString('Success', i)
