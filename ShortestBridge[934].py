# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1

# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2

# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1

 

# Constraints:

#     n == grid.length == grid[i].length
#     2 <= n <= 100
#     grid[i][j] is either 0 or 1.
#     There are exactly two islands in grid.

# Accepted
# 160,155
# Submissions
# 279,360

from collections import deque


class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        queue = deque()
        found = False

        # Поиск первого острова и добавление его вершин в очередь
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, queue)
                    found = True
                    break

        # Поиск границы между островами с помощью BFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min_flips = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return min_flips  # Мы достигли другого острова, возвращаем минимальное количество переворотов

                        if grid[nx][ny] == 0:
                            grid[nx][ny] = -1  # Помечаем границу между островами
                            queue.append((nx, ny))

            min_flips += 1

        return min_flips


    def dfs(self,grid, i, j, queue):
        n = len(grid)
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return

        grid[i][j] = -1  # Помечаем посещенные вершины первого острова
        queue.append((i, j))  # Добавляем вершины первого острова в очередь

        self.dfs(grid, i - 1, j, queue)
        self.dfs(grid, i + 1, j, queue)
        self.dfs(grid, i, j - 1, queue)
        self.dfs(grid, i, j + 1, queue)


list_num = [[0,1],[1,0]],[[0,1,0],[0,0,0],[0,0,1]],[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
for i in list_num:
    Solution.shortestBridge('Success', i)