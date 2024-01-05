# 79. Word Search
# Medium

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

 

# Constraints:

#     m == board.length
#     n = board[i].length
#     1 <= m, n <= 6
#     1 <= word.length <= 15
#     board and word consists of only lowercase and uppercase English letters.

 

# Follow up: Could you use search pruning to make your solution faster with a larger board?
# Accepted
# 1,324,078
# Submissions
# 3,272,465


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k):
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False            
            if k == len(word) - 1:
                return True
            temp, board[i][j] = board[i][j], '/'
            result = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = temp            
            return result  
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True                
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED",  "SEE", "ABCB"
for index, w in enumerate(board):
  Solution.exist('Success', w, word[index])
