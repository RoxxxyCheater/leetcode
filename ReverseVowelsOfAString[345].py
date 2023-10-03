# 345. Reverse Vowels of a String
# Easy

# 4031

# 2666

# Add to List

# Share
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.
# Accepted
# 629,317
# Submissions
# 1,225,720

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """       
        # Преобразуем входную строку в список для удобства модификации
        s = list(s)
        гласные = "aeiouAEIOU"  # Задаем строку, содержащую все гласные буквы
        
        # Инициализируем два указателя в начале и конце строки
        левый, правый = 0, len(s) - 1
        
        while левый < правый:
            # Перемещаем левый указатель вправо, пока он не указывает на гласную букву
            while левый < правый and s[левый] not in гласные:
                левый += 1
            
            # Перемещаем правый указатель влево, пока он не указывает на гласную букву
            while левый < правый and s[правый] not in гласные:
                правый -= 1
            
            # Меняем местами гласные, на которые указывают левый и правый указатели
            s[левый], s[правый] = s[правый], s[левый]
            
            # Перемещаем указатели к центру
            левый += 1
            правый -= 1
        
        # Преобразуем список обратно в строку и возвращаем результат
        return "".join(s)



list_s = "hello", "leetcode"
for i in list_s:
   Solution.reverseVowels('Success', i)
