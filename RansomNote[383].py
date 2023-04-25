
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

 

# Constraints:

#     1 <= ransomNote.length, magazine.length <= 105
#     ransomNote and magazine consist of lowercase English letters.

# Accepted
# 744.4K
# Submissions
# 1.3M
# Acceptance Rate
# 58.3%

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = {} #Словарь для храниния букв из журнала
        for c in magazine: # перебираем журнал
            if c in mag_dict:
                mag_dict[c] += 1 # пересчитываем колическвто если буква в словаре
            else:
                mag_dict[c] = 1 # Добавляем 1 букву если её ещё нет в словаре
        for c in ransomNote: # Перебираем ransomeNote 
            if c not in mag_dict or mag_dict[c] == 0: # Если буквы нет или колл-во 0
                return False # Отсекаем
            mag_dict[c] -= 1 # шаг перебора
        return True # если перебрали все буквы в ransomNote, значит, мы можно построить его из magazine
    

ransomNote_list = "a", "aa", "aa"
magazine_list = "b", "ab", "aab"

for index, strs in enumerate(ransomNote_list):
    Solution.canConstruct('Succes',strs, magazine_list[index])