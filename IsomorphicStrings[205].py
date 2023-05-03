# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true

# Example 2:

# Input: s = "foo", t = "bar"
# Output: false

# Example 3:

# Input: s = "paper", t = "title"
# Output: true

 

# Constraints:

#     1 <= s.length <= 5 * 104
#     t.length == s.length
#     s and t consist of any valid ascii character.

# Accepted
# 882.8K
# Submissions
# 2.1M
# Acceptance Rate
# 43.0%
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Создаем две пустые хэш-таблицы для отображения символов из s в t и из t в s соответственно
        s_to_t = {}
        t_to_s = {}
        # Проходим по всем символам в s и t одновременно
        for i in range(len(s)):
            # Если текущий символ из s еще не отображался на символ в t,
            # и текущий символ из t еще не отображался на символ в s
            if s[i] not in s_to_t and t[i] not in t_to_s:
                # Добавляем соответствующее отображение в обе хэш-таблицы
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            # Если текущий символ из s уже отображался на символ в t
            # ИЛИ текущий символ из t уже отображался на символ в s
            elif s_to_t.get(s[i]) != t[i] or t_to_s.get(t[i]) != s[i]:
                # То строки не изоморфны, возвращаем False
                return False
        # Если мы успешно прошли по всем символам и не нашли несоответствия,
        # то строки изоморфны, возвращаем True
        return True



list_strs = "egg","foo","paper"
list_strt = "add","bar","title"
for index, strs in enumerate(list_strs):
    Solution.secondHighest('Success', strs)