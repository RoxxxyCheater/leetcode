# 821. Shortest Distance to a Character
# Easy

# 3033

# 156

# Add to List

# Share
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

 

# Example 1:

# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
# Example 2:

# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]
 

# Constraints:

# 1 <= s.length <= 104
# s[i] and c are lowercase English letters.
# It is guaranteed that c occurs at least once in s.
# Accepted
# 170,885
# Submissions
# 239,563
class Solution(object):
 
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        # Создаем массив result, заполненный бесконечно большими значениями.
        result = [float('inf')] * n
    
        # Проход вперёд: вычисляем расстояние до ближайшего вхождения 'c' справа.
        last_seen_index = float('-inf')
        for i in range(n):
            # Обновляем last_seen_index, если текущий символ - 'c'.
            if s[i] == c:
                last_seen_index = i
            # Вычисляем расстояние от текущего индекса до последнего вхождения 'c' и обновляем результат.
            result[i] = min(result[i], abs(i - last_seen_index))
    
        # Проход назад: вычисляем расстояние до ближайшего вхождения 'c' слева.
        last_seen_index = float('inf')
        for i in range(n - 1, -1, -1):
            # Обновляем last_seen_index, если текущий символ - 'c'.
            if s[i] == c:
                last_seen_index = i
            # Вычисляем расстояние от текущего индекса до последнего вхождения 'c' и обновляем результат.
            result[i] = min(result[i], abs(i - last_seen_index))
    
        # Возвращаем итоговый массив расстояний.
        return result

list_s =  "loveleetcode", "aaab"
list_c =  "e", "b"

for index, s in enumerate(list_s):
   Solution.shortestToChar('Success', s, list_c[index])
