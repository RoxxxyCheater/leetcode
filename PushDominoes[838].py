# 838. Push Dominoes
# Medium

# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:

#     dominoes[i] = 'L', if the ith domino has been pushed to the left,
#     dominoes[i] = 'R', if the ith domino has been pushed to the right, and
#     dominoes[i] = '.', if the ith domino has not been pushed.

# Return a string representing the final state.

 

# Example 1:

# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.

# Example 2:

# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

 

# Constraints:

#     n == dominoes.length
#     1 <= n <= 105
#     dominoes[i] is either 'L', 'R', or '.'.

# Accepted
# 118,008
# Submissions
# 206,795


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """

        n = len(dominoes)
        forces = [0] * n  # Создаем массив, чтобы хранить силы, действующие на каждый домино.

        # Рассчитываем силы, действующие вправо
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # Если домино движется вправо ('R'), устанавливаем силу в n.
            elif dominoes[i] == 'L':
                force = 0  # Если домино движется влево ('L'), сила сбрасывается в 0.
            else:
                force = max(force - 1, 0)  # В остальных случаях уменьшаем силу на 1, но не меньше 0.
            forces[i] += force  # Добавляем силу к текущему домино.

        # Рассчитываем силы, действующие влево
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n  # Если домино движется влево ('L'), устанавливаем силу в n.
            elif dominoes[i] == 'R':
                force = 0  # Если домино движется вправо ('R'), сила сбрасывается в 0.
            else:
                force = max(force - 1, 0)  # В остальных случаях уменьшаем силу на 1, но не меньше 0.
            forces[i] -= force  # Вычитаем силу из текущего домино.

        # Обновляем состояние домино на основе вычисленных сил
        result = []
        for force in forces:
            if force > 0:
                result.append('R')  # Если сила положительная, домино движется вправо ('R').
            elif force < 0:
                result.append('L')  # Если сила отрицательная, домино движется влево ('L').
            else:
                result.append('.')  # Если сила равна 0, домино стоит на месте ('.').
        return ''.join(result)  # Преобразуем результат в строку и возвращаем его.

list_d = "RR.L", ".L.R...LR..L.."
for i in list_d:
    Solution.pushDominoes('Success', i)
