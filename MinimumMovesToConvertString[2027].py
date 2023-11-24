# 2027. Minimum Moves to Convert String
# Easy

# You are given a string s consisting of n characters which are either 'X' or 'O'.

# A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

# Return the minimum number of moves required so that all the characters of s are converted to 'O'.

 

# Example 1:

# Input: s = "XXX"
# Output: 1
# Explanation: XXX -> OOO
# We select all the 3 characters and convert them in one move.

# Example 2:

# Input: s = "XXOX"
# Output: 2
# Explanation: XXOX -> OOOX -> OOOO
# We select the first 3 characters in the first move, and convert them to 'O'.
# Then we select the last 3 characters and convert them so that the final string contains all 'O's.

# Example 3:

# Input: s = "OOOO"
# Output: 0
# Explanation: There are no 'X's in s to convert.

 

# Constraints:

#     3 <= s.length <= 1000
#     s[i] is either 'X' or 'O'.

# Accepted
# 31,912
# Submissions
# 58,588


class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves = 0 # инициализируем кол-во хходов
         
         i = 0 
         while i < len(s): # Проходим циклом while 
             if s[i] == 'X': # Если буква в слове искома
                 moves += 1 # Прибавляем ход
                 i += 3 
             else:
                 i += 1 #иначе отнимаем
         
         return moves

list_s = "XXX", "XXOX"
for i in list_s:
   Solution.minimumMoves('Success', i)
