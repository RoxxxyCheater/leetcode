# 884. Uncommon Words from Two Sentences
# Easy

# 1301

# 164

# Add to List

# Share
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
 

# Constraints:

# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
# Accepted
# 129,671
# Submissions
# 194,113


class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        def get_word_count(sentence):
            words = sentence.split()
            return Counter(words)
        count_s1 = get_word_count(s1)
        count_s2 = get_word_count(s2)
        uncommon_words = []
        for word, count in count_s1.items():
            if count == 1 and word not in count_s2:
                uncommon_words.append(word)
        for word, count in count_s2.items():
            if count == 1 and word not in count_s1:
                uncommon_words.append(word)
        return uncommon_words

list_s = "this apple is sweet", "apple apple"
list_ss = "this apple is sour", "banana"

for i, s in enumerate(list_s):
   Solution.uncommonFromSentences('Success', s, list_ss[i])
