# 1704. Determine if String Halves Are Alike
# Easy
# 1.8K
# 81
# Companies
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

 

# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.
 

# Constraints:

# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.
# Accepted
# 198.9K
# Submissions
# 256.7K
# Acceptance Rate
# 77.5%


class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Функция для подсчета гласных в строке
        def countVowels(substring):
            vowels = set("aeiouAEIOU")
            count = 0
            for char in substring:
                if char in vowels:
                    count += 1
            return count

        # Разделяем строку на две половины
        length = len(s)
        half_length = length // 2
        a = s[:half_length]
        b = s[half_length:]

        # Подсчитываем гласные для каждой половины и сравниваем
        count_a = countVowels(a)
        count_b = countVowels(b)

        return count_a == count_b



list_s = "book", "textbook"
for i in list_s:
   Solution.halvesAreAliske('Success', i)
