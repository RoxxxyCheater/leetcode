
# Medium

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

 

# Constraints:

#     1 <= n <= 200
#     n == isConnected.length
#     n == isConnected[i].length
#     isConnected[i][j] is 1 or 0.
#     isConnected[i][i] == 1
#     isConnected[i][j] == isConnected[j][i]

# Accepted
# 664,132
# Submissions
# 1,026,177


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)  # Получаем общее количество городов (размер матрицы)
        visited = [False] * n  # Создаем булев массив для отслеживания посещенных городов
        provinces = 0  # Инициализируем переменную для подсчета общего числа провинций

        def dfs(city, visited):
            visited[city] = True  # Отмечаем текущий город как посещенный
            for i in range(n):  # Итерируемся по всем городам
                if isConnected[city][i] == 1 and not visited[i]:  # Проверяем, связан ли город непосредственно и не посещался ли он ранее
                    dfs(i, visited)  # Рекурсивно вызываем функцию dfs для связанного города

        for city in range(n):  # Итерируемся по всем городам
            if not visited[city]:  # Если город не был посещен
                dfs(city, visited)  # Вызываем функцию dfs для исследования связанных городов
                provinces += 1  # Увеличиваем счетчик провинций

        return provinces  # Возвращаем общее число провинций
    
is_list = [[1,1,0],[1,1,0],[0,0,1]],[[1,0,0],[0,1,0],[0,0,1]]
for i in is_list:
   Solution.findCircleNum('Success', i)
