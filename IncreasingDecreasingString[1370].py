# 1370. Increasing Decreasing String
# Easy

# You are given a string s. Reorder the string using the following algorithm:

#     Pick the smallest character from s and append it to the result.
#     Pick the smallest character from s which is greater than the last appended character to the result and append it.
#     Repeat step 2 until you cannot pick more characters.
#     Pick the largest character from s and append it to the result.
#     Pick the largest character from s which is smaller than the last appended character to the result and append it.
#     Repeat step 5 until you cannot pick more characters.
#     Repeat the steps from 1 to 6 until you pick all characters from s.

# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

# Return the result string after sorting s with this algorithm.

 

# Example 1:

# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

# Example 2:

# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

 

# Constraints:

#     1 <= s.length <= 500
#     s consists of only lowercase English letters.

# Accepted
# 71,728
# Submissions
# 93,896


class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []  # Результирующая строка
        s_list = list(s)  # Преобразуем строку в список символов
        
        while s_list:
            # Шаг 1: Выбор самого маленького символа
            smallest = min(s_list)
            result.append(smallest)
            s_list.remove(smallest)
            
            # Шаг 2: Выбор самого маленького символа, большего, чем последний добавленный символ
            for char in sorted(set(s_list)):
                if char > result[-1]:
                    result.append(char)
                    s_list.remove(char)
            
            # Проверка наличия оставшихся символов
            if not s_list:
                break
            
            # Шаг 4: Выбор самого большого символа
            largest = max(s_list)
            result.append(largest)
            s_list.remove(largest)
            
            # Шаг 5: Выбор самого большого символа, меньшего, чем последний добавленный символ
            for char in sorted(set(s_list), reverse=True):
                if char < result[-1]:
                    result.append(char)
                    s_list.remove(char)
        
        return ''.join(result)

ls= "aaaabbbbcccc", "rat"

for i in ls:
   Solution.sortString('Success', i)
