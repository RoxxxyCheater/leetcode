# 2053. Kth Distinct String in an Array
# Easy

# 714

# 26

# Add to List

# Share
# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

 

# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned. 
# Example 2:

# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.
# Example 3:

# Input: arr = ["a","b","a"], k = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
 

# Constraints:

# 1 <= k <= arr.length <= 1000
# 1 <= arr[i].length <= 5
# arr[i] consists of lowercase English letters.
# Accepted
# 54,164
# Submissions
# 74,920


class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # Создаем словарь с подсчетом уникальных строк в массиве
        string_count = Counter(arr)

        # Сортируем словарь с учетом порядка появления строк в оригинальном массиве
        ordered_dict = OrderedDict(sorted(string_count.items(), key=lambda x: arr.index(x[0])))

        # Перебираем отсортированный словарь
        for string, count in ordered_dict.items():
            # Если строка встречается только один раз
            if count == 1:
                # Уменьшаем значение k
                k -= 1
                # Когда k достигает нуля, возвращаем эту строку
                if k == 0:
                    return string

        # Если уникальных строк меньше, чем k, возвращаем пустую строку
        return ""

al = ["d","b","c","b","c","a"], ["aaa","aa","a"], ["a","b","a"]
kl = 2, 1, 3

for i, a in enumerate(al):
   Solution.kthDistinct('Success', a, kl[i])
