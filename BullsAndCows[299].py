# 299. Bulls and Cows
# Medium

# 2320

# 1762

# Add to List

# Share
# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
 

# Constraints:

# 1 <= secret.length, guess.length <= 1000
# secret.length == guess.length
# secret and guess consist of digits only.
# Accepted
# 359,778
# Submissions
# 720,917



class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # Инициализируем счетчики для быков и коров
        bulls = 0
        cows = 0
        # Инициализируем словари для подсчета вхождений цифр в строках secret и guess
        secret_count = {}
        guess_count = {}
    
        # Подсчет быков и заполнение словарей
        for s, g in zip(secret, guess):
            # Если цифры на одинаковых позициях совпадают, увеличиваем счетчик быков
            if s == g:
                bulls += 1
            else:
                # Иначе увеличиваем счетчик вхождений цифры в соответствующем словаре
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1
    
        # Подсчет коров
        for g, count in guess_count.items():
            # Для каждой цифры в guess смотрим, сколько таких же цифр есть в secret
            # и прибавляем минимум из этих значений к счетчику коров
            cows += min(count, secret_count.get(g, 0))
    
        # Возвращаем результат в формате "xAyB", где x - количество быков, y - количество коров
        return "{}A{}B".format(bulls, cows)


list_s = "1807", "1123"
list_g = "7810", "0111"
for i, s in enumerate(list_s):
   Solution.getHint('Success', s, list_g[i])
