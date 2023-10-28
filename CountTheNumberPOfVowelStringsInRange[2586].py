# 2586. Count the Number of Vowel Strings in Range
# Easy

# You are given a 0-indexed array of string words and two integers left and right.

# A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

 

# Example 1:

# Input: words = ["are","amy","u"], left = 0, right = 2
# Output: 2
# Explanation: 
# - "are" is a vowel string because it starts with 'a' and ends with 'e'.
# - "amy" is not a vowel string because it does not end with a vowel.
# - "u" is a vowel string because it starts with 'u' and ends with 'u'.
# The number of vowel strings in the mentioned range is 2.

# Example 2:

# Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
# Output: 3
# Explanation: 
# - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
# - "mu" is not a vowel string because it does not start with a vowel.
# - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
# - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
# The number of vowel strings in the mentioned range is 3.

 

# Constraints:

#     1 <= words.length <= 1000
#     1 <= words[i].length <= 10
#     words[i] consists of only lowercase English letters.
#     0 <= left <= right < words.length

# Accepted
# 45,431
# Submissions
# 61,358


class Solution(object):
    def is_vowel_string(self, word):
        vowels = "aeiou"
        return word[0] in vowels and word[-1] in vowels
     
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0
        for i in range(left, right + 1):
            if self.is_vowel_string(words[i]):
                count += 1
        return count

list_w = ["are","amy","u"], ["hey","aeo","mu","ooo","artro"]
list_l = 0, 1
list_r = 2, 4
for index, word in enumerate(list_w):
  Solution.voweStrings('Success', word, list_l[index], list_r[index])

