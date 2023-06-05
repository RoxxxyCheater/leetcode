# There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 

# Example 1:

# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

# Example 2:

# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

 

# Constraints:

#     1 <= moves.length <= 2 * 104
#     moves only contains the characters 'U', 'D', 'L' and 'R'.

# Accepted
# 373,239
# Submissions
# 495,273


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0  # Инициализируем координату x робота
        y = 0  # Инициализируем координату y робота

        for move in moves:  # Проходимся по каждому символу в строке moves
            if move == 'U':  # Если символ равен 'U'
                y += 1  # Увеличиваем координату y на 1
            elif move == 'D':  # Если символ равен 'D'
                y -= 1  # Уменьшаем координату y на 1
            elif move == 'L':  # Если символ равен 'L'
                x -= 1  # Уменьшаем координату x на 1
            elif move == 'R':  # Если символ равен 'R'
                x += 1  # Увеличиваем координату x на 1

        return x == 0 and y == 0  # Возвращаем True, если робот вернулся в исходную точку (координаты x и y равны 0), иначе возвращаем False

    
list_move = "UP", "LL"
for i in list_move:
   Solution.judgeCircle('Success', i)
