# 2606. Find the Substring With Maximum Cost
# Medium

# You are given a string s, a string chars of distinct characters and an integer array vals of the same length as chars.

# The cost of the substring is the sum of the values of each character in the substring. The cost of an empty string is considered 0.

# The value of the character is defined in the following way:

#     If the character is not in the string chars, then its value is its corresponding position (1-indexed) in the alphabet.
#         For example, the value of 'a' is 1, the value of 'b' is 2, and so on. The value of 'z' is 26.
#     Otherwise, assuming i is the index where the character occurs in the string chars, then its value is vals[i].

# Return the maximum cost among all substrings of the string s.

 

# Example 1:

# Input: s = "adaa", chars = "d", vals = [-1000]
# Output: 2
# Explanation: The value of the characters "a" and "d" is 1 and -1000 respectively.
# The substring with the maximum cost is "aa" and its cost is 1 + 1 = 2.
# It can be proven that 2 is the maximum cost.

# Example 2:

# Input: s = "abc", chars = "abc", vals = [-1,-1,-1]
# Output: 0
# Explanation: The value of the characters "a", "b" and "c" is -1, -1, and -1 respectively.
# The substring with the maximum cost is the empty substring "" and its cost is 0.
# It can be proven that 0 is the maximum cost.

 

# Constraints:

#     1 <= s.length <= 105
#     s consist of lowercase English letters.
#     1 <= chars.length <= 26
#     chars consist of distinct lowercase English letters.
#     vals.length == chars.length
#     -1000 <= vals[i] <= 1000

# Accepted
# 19,869
# Submissions
# 35,549



class Solution(object):
    def maximumCostSubstring(self, s, chars, vals):
        """
        :type s: str
        :type chars: str
        :type vals: List[int]
        :rtype: int
        """
        char_values = {}  # Словарь для хранения значений символов

        # Заполняем словарь значениями символов из chars и соответствующими им значениями из vals
        for i, char in enumerate(chars):
            char_values[char] = vals[i]

        max_cost = 0  # Переменная для хранения максимальной стоимости
        current_cost = 0  # Переменная для хранения текущей стоимости подстроки
        left = 0  # Левый указатель скользящего окна

        # Проходим по строке s с помощью правого указателя (right)
        for right in range(len(s)):
            if s[right] in char_values:
                # Если символ есть в chars, добавляем его значение к текущей стоимости
                current_cost += char_values[s[right]]
            else:
                # Если символа нет в chars, вычисляем его значение по алфавиту и добавляем к текущей стоимости
                current_cost += ord(s[right]) - ord('a') + 1

            # Проверяем условие, если текущая стоимость стала отрицательной
            while current_cost < 0:
                if s[left] in char_values:
                    # Если символ есть в chars, вычитаем его значение из текущей стоимости
                    current_cost -= char_values[s[left]]
                else:
                    # Если символа нет в chars, вычитаем его значение по алфавиту из текущей стоимости
                    current_cost -= ord(s[left]) - ord('a') + 1
                left += 1  # Увеличиваем левый указатель, смещая окно вправо

            # Обновляем максимальную стоимость, если текущая стоимость больше
            max_cost = max(max_cost, current_cost)

        return max_cost




list_s = "adaa", "abc"
list_c = "d", "abc"
list_v = [-1000], [-1,-1,-1]


for index, s in enumerate(list_s):
    Solution.maximumCostSubstring('Success', s, list_c[index], list_v[index])
