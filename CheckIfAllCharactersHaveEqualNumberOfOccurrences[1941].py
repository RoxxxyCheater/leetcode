# 1941. Check if All Characters Have Equal Number of Occurrences
# Easy

# 822

# 20

# Add to List

# Share
# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# Accepted
# 81,509
# Submissions
# 105,877



class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        # Создаем словарь для отслеживания количества вхождений каждого символа
        char_count = {}
        
        # Подсчитываем количество вхождений каждого символа в строке
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Создаем список, содержащий частоты вхождений каждого символа
        frequencies = list(char_count.values())
        
        # Проверяем, имеют ли все символы одинаковую частоту
        return all(frequency == frequencies[0] for frequency in frequencies)

     
l_s = "abacbc", "aaabb"
for s in l_s:
   Solution.areOccurrencesEqual('Success', s)
