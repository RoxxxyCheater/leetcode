# 1684. Count the Number of Consistent Strings
# Easy

# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

 

# Example 1:

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# Example 2:

# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.

# Example 3:

# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

 

# Constraints:

#     1 <= words.length <= 104
#     1 <= allowed.length <= 26
#     1 <= words[i].length <= 10
#     The characters in allowed are distinct.
#     words[i] and allowed contain only lowercase English letters.

# Accepted
# 154,974
# Submissions
# 187,443


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # Convert the allowed string to a set for faster lookup
        allowed_set = set(allowed)

        # Initialize a counter for consistent strings
        count = 0

        # Iterate through each word in the words array
        for word in words:
            # Check if all characters in the word are in the allowed set
            if all(char in allowed_set for char in word):
                # Increment the counter if the word is consistent
                count += 1

        return count

list_a ="ab", "abc", "cad"
list_w = ["ad","bd","aaab","baa","badab"],["a","b","c","ab","ac","bc","abc"], ["cc","acd","b","ba","bac","bad","ac","d"]

for w, a in enumerate(list_a):
   Solution.countConsistentStrings('Success', a, list_w[w])
