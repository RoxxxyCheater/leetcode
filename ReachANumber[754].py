# 754. Reach a Number
# Medium

# 1710

# 768

# Add to List

# Share
# You are standing at position 0 on an infinite number line. There is a destination at position target.

# You can make some number of moves numMoves so that:

# On each move, you can either go left or right.
# During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
# Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.

 

# Example 1:

# Input: target = 2
# Output: 3
# Explanation:
# On the 1st move, we step from 0 to 1 (1 step).
# On the 2nd move, we step from 1 to -1 (2 steps).
# On the 3rd move, we step from -1 to 2 (3 steps).
# Example 2:

# Input: target = 3
# Output: 2
# Explanation:
# On the 1st move, we step from 0 to 1 (1 step).
# On the 2nd move, we step from 1 to 3 (2 steps).
 

# Constraints:

# -109 <= target <= 109
# target != 0
# Accepted
# 49,758
# Submissions
# 116,153


class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # Преобразуем значение target в положительное для упрощения вычислений
        target = abs(target)

        # Инициализируем переменную для отслеживания текущей позиции
        position = 0

        # Инициализируем переменную для отслеживания текущего хода
        move = 0

        # Продолжаем двигаться, пока текущая позиция не станет больше или равной цели,
        # учитывая возможность движения влево и вправо
        while position < target or (position - target) % 2 != 0:
            move += 1
            position += move

        # Возвращаем минимальное количество ходов, необходимых для достижения цели
        return move



list_t = 2,3
for i in list_t:
  Solution. reachNumber('Success', i)
