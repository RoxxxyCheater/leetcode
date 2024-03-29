# 1138. Alphabet Board Path
# Medium
# 859
# 171
# Companies
# On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



# We may make the following moves:

# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the board;
# 'R' moves our position right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the answer.
# (Here, the only positions that exist on the board are positions with letters on them.)

# Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

# Example 1:

# Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"
# Example 2:

# Input: target = "code"
# Output: "RR!DDRR!UUL!R!"
 

# Constraints:

# 1 <= target.length <= 100
# target consists only of English lowercase letters.
# Accepted
# 48.8K
# Submissions
# 94.2K
# Acceptance Rate
# 51.9%


class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        # Создаем словарь для хранения координат каждой буквы
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        char_to_coords = {}
        for r, row in enumerate(board):
            for c, char in enumerate(row):
                char_to_coords[char] = (r, c)

        # Инициализируем начальную позицию
        r, c = 0, 0
        result = []  # Здесь будем хранить последовательность ходов

        for char in target:
            tr, tc = char_to_coords[char]  # Координаты целевой буквы
            while r > tr:
                result.append('U')  # Двигаемся вверх
                r -= 1
            while c < tc:
                result.append('R')  # Двигаемся вправо
                c += 1
            while c > tc:
                result.append('L')  # Двигаемся влево
                c -= 1
            while r < tr:
                result.append('D')  # Двигаемся вниз
                r += 1
            result.append('!')  # Добавляем букву к ответу

        return ''.join(result)  # Возвращаем последовательность ходов


 list_t = "leet", "code"
for i in list_t:
  Solution.alphabetBoardPath('Success', i)
