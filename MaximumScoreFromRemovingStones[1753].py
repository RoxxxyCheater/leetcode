# 1753. Maximum Score From Removing Stones
# Medium

# 887

# 53

# Add to List

# Share
# You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

# Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.

 

# Example 1:

# Input: a = 2, b = 4, c = 6
# Output: 6
# Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
# - Take from 1st and 3rd piles, state is now (1, 4, 5)
# - Take from 1st and 3rd piles, state is now (0, 4, 4)
# - Take from 2nd and 3rd piles, state is now (0, 3, 3)
# - Take from 2nd and 3rd piles, state is now (0, 2, 2)
# - Take from 2nd and 3rd piles, state is now (0, 1, 1)
# - Take from 2nd and 3rd piles, state is now (0, 0, 0)
# There are fewer than two non-empty piles, so the game ends. Total: 6 points.
# Example 2:

# Input: a = 4, b = 4, c = 6
# Output: 7
# Explanation: The starting state is (4, 4, 6). One optimal set of moves is:
# - Take from 1st and 2nd piles, state is now (3, 3, 6)
# - Take from 1st and 3rd piles, state is now (2, 3, 5)
# - Take from 1st and 3rd piles, state is now (1, 3, 4)
# - Take from 1st and 3rd piles, state is now (0, 3, 3)
# - Take from 2nd and 3rd piles, state is now (0, 2, 2)
# - Take from 2nd and 3rd piles, state is now (0, 1, 1)
# - Take from 2nd and 3rd piles, state is now (0, 0, 0)
# There are fewer than two non-empty piles, so the game ends. Total: 7 points.
# Example 3:

# Input: a = 1, b = 8, c = 8
# Output: 8
# Explanation: One optimal set of moves is to take from the 2nd and 3rd piles for 8 turns until they are empty.
# After that, there are fewer than two non-empty piles, so the game ends.
 

# Constraints:

# 1 <= a, b, c <= 105
# Accepted
# 35,524
# Submissions
# 52,628


class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        nums = [a, b, c]
        score = 0
        nums.sort(reverse=True)
        while nums[1] > 0:
            nums[0] -= 1
            nums[1] -= 1
            score += 1
            nums.sort(reverse=True)
        return score

list_a = 2, 4, 1
list_b = 4, 4, 8
list_c = 6, 6, 8

for index, num in enumerate(list_a)
  Solution.maximumScore('Success', num, list_b[index], list_c[index])
