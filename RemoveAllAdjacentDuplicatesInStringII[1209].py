# 1209. Remove All Adjacent Duplicates in String II
# Medium

# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.

# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"

 

# Constraints:

#     1 <= s.length <= 105
#     2 <= k <= 104
#     s only contains lowercase English letters.

# Accepted
# 294,272
# Submissions
# 515,569


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []  # Используем стек для отслеживания символов и их количества
    
        for char in s:
            if stack and stack[-1][0] == char:
                # Если текущий символ равен вершине стека, увеличиваем количество повторений
                stack[-1] = (char, stack[-1][1] + 1)
                if stack[-1][1] == k:
                    # Если количество повторений достигло k, удаляем вершину стека
                    stack.pop()
            else:
                # Иначе добавляем текущий символ с количеством 1 в стек
                stack.append((char, 1))
    
        result = ''
        for char, count in stack:
            # Собираем окончательный результат, объединяя символы с их количеством
            result += char * count
    
        return result

l_s = "abcd", "deeedbbcccbdaa", "pbbcggttciiippooaais"
l_k = 2, 3, 2

for k, s in enumerate(l_s):
   Soluiton.removeDuplicates('Success', s, l_k[k])
