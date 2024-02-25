# 1025. Divisor Game
# Description
# Hints
# Submissions
# Discuss
# Solution
# Pick One
# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

# Choosing any x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game.

# Return true if and only if Alice wins the game, assuming both players play optimally.

 

# Example 1:

# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# Example 2:

# Input: n = 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

# Constraints:

# 1 <= n <= 1000


class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Создаем массив dp, в котором будем хранить результаты игры для чисел от 1 до n
        dp = [False] * (n + 1)
        # Базовый случай: для n = 1 Alice не может сделать ход и проигрывает
        dp[1] = False
        
        # Начинаем заполнение массива dp, начиная с числа 2
        for i in range(2, n + 1):
            # Перебираем все возможные делители числа i
            for j in range(1, i):
                # Если число i делится на j без остатка и при этом Alice проигрывает при числе (i - j),
                # то при числе i Alice выигрывает
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break
        
        # Возвращаем результат игры для числа n
        return dp[n]
ln = 2, 3

for n in ln:
   Solution.divisorGame('Success', n)
