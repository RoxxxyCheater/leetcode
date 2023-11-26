# 2085. Count Common Words With One Occurrence
# Easy

# 738

# 16

# Add to List

# Share
# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

 

# Example 1:

# Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
# Output: 2
# Explanation:
# - "leetcode" appears exactly once in each of the two arrays. We count this string.
# - "amazing" appears exactly once in each of the two arrays. We count this string.
# - "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
# - "as" appears once in words1, but does not appear in words2. We do not count this string.
# Thus, there are 2 strings that appear exactly once in each of the two arrays.
# Example 2:

# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.
# Example 3:

# Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
# Output: 1
# Explanation: The only string that appears exactly once in each of the two arrays is "ab".
 

# Constraints:

# 1 <= words1.length, words2.length <= 1000
# 1 <= words1[i].length, words2[j].length <= 30
# words1[i] and words2[j] consists only of lowercase English letters.
# Accepted
# 55,848
# Submissions
# 80,029





class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        word_count1 = {}
        word_count2 = {}
        for word in words1:
            word_count1[word] = word_count1.get(word, 0) + 1
        for word in words2:
            word_count2[word] = word_count2.get(word, 0) + 1    
        count = 0
        for word in set(words1 + words2):
            count += (word_count1.get(word, 0) == 1) and (word_count2.get(word, 0) == 1)
        return count


list_w = ["leetcode","is","amazing","as","is"], ["b","bb","bbb"], ["a","ab"]
list_ww = ["amazing","leetcode","is"], ["a","aa","aaa"],  ["a","a","a","ab"]

for i, w in enumerate(list_w):
   Solution.countWords('Success', w, list_ww[i])
