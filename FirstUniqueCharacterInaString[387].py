# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.
# Accepted
# 1.4M
# Submissions
# 2.3M
# Acceptance Rate
# 59.7%


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}  # Создаем пустой словарь для хранения количества вхождений каждого символа
        for c in s:
            if c in count:
                count[c] += 1  # Если символ уже встречался, увеличиваем количество его вхождений на 1
            else:
                count[c] = 1  # Если символ встречается впервые, добавляем его в словарь и устанавливаем количество вхождений равным 1

        for i in range(len(s)):
            if count[s[i]] == 1:  # Ищем первый символ, количество вхождений которого равно 1
                return i  # Если такой символ найден, возвращаем его индекс в строке

        return -1  # Если такой символ не найден, возвращаем -1
       

       
       
       
       
       
list_s = "leetcode","loveleetcode", "aabb"
for i in list_s:
 Solution.firstUniqChar('Success', i)
