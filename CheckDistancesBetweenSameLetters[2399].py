# 2399. Check Distances Between Same Letters
# Easy

# 439

# 47

# Add to List

# Share
# You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.

# Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

# In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.

# Return true if s is a well-spaced string, otherwise return false.

 

# Example 1:

# Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: true
# Explanation:
# - 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
# - 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
# - 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
# Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
# Return true because s is a well-spaced string.
# Example 2:

# Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: false
# Explanation:
# - 'a' appears at indices 0 and 1 so there are zero letters between them.
# Because distance[0] = 1, s is not a well-spaced string.
 

# Constraints:

# 2 <= s.length <= 52
# s consists only of lowercase English letters.
# Each letter appears in s exactly twice.
# distance.length == 26
# 0 <= distance[i] <= 50
# Accepted
# 41,833
# Submissions
# 59,731


class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        # Создаем словарь для хранения индексов первого и второго появления каждой буквы.
        letter_indices = {chr(i): [] for i in range(ord('a'), ord('z') + 1)}
    
        # Итерируемся по строке, чтобы найти индексы первых появлений букв.
        for i, letter in enumerate(s):
            letter_index = ord(letter) - ord('a')
            letter_indices[letter].append(i)
    
        # Проверяем, удовлетворяют ли расстояния для каждой буквы условиям.
        for letter, indices in letter_indices.items():
            if len(indices) == 2:
                # Если буква появляется дважды, вычисляем разницу между индексами и проверяем с заданным расстоянием.
                diff = indices[1] - indices[0] - 1
                if diff != distance[ord(letter) - ord('a')]:
                    return False
            elif len(indices) > 0:
                # Если буква появляется только один раз, но её расстояние не равно 0, возвращаем False.
                if distance[ord(letter) - ord('a')] != 0:
                    return False
    
        # Если все буквы удовлетворяют условиям, возвращаем True.
        return True


list_s = "abaccb", "aa"
list_d = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for inddex, s in enumerate(list_s):
   Solution.checkDistances('Success', s, list_d[index])
