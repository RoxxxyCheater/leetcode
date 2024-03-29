# 2609. Find the Longest Balanced Substring of a Binary String
# Easy

# 347

# 21

# Add to List

# Share
# You are given a binary string s consisting only of zeroes and ones.

# A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

# Return the length of the longest balanced substring of s.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "01000111"
# Output: 6
# Explanation: The longest balanced substring is "000111", which has length 6.
# Example 2:

# Input: s = "00111"
# Output: 4
# Explanation: The longest balanced substring is "0011", which has length 4. 
# Example 3:

# Input: s = "111"
# Output: 0
# Explanation: There is no balanced substring except the empty substring, so the answer is 0.
 

# Constraints:

# 1 <= s.length <= 50
# '0' <= s[i] <= '1'
# Accepted
# 28,108
# Submissions
# 61,405


class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0  # Переменная для отслеживания максимальной длины сбалансированной подстроки
        balance = 0  # Переменная для отслеживания баланса (разницы между количеством '0' и '1')
    
        for i in range(len(s)):
            if s[i] == '0':
                balance += 1  # Увеличиваем баланс при встрече '0'
            else:
                balance -= 1  # Уменьшаем баланс при встрече '1'
    
            if balance == 0:
                # Если баланс становится равным 0, значит, найдена сбалансированная подстрока
                # Обновляем максимальную длину с учетом текущей позиции i
                max_length = max(max_length, i + 1)
            elif balance < 0:
                # Если баланс становится отрицательным, сбрасываем его в 0,
                # так как сбалансированная подстрока не может начинаться с отрицательного баланса
                balance = 0
    
        return max_length

l_s = "01000111", "00111", "111"

for s in l_s:
   Solution.findTheLongestBalancedSubstring('Success', s)
