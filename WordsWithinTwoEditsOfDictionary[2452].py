# 2452. Words Within Two Edits of Dictionary
# Medium

# 262

# 17

# Add to List

# Share
# You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.

# In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

# Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.

 

# Example 1:

# Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
# Output: ["word","note","wood"]
# Explanation:
# - Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
# - Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
# - It would take more than 2 edits for "ants" to equal a dictionary word.
# - "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
# Thus, we return ["word","note","wood"].
# Example 2:

# Input: queries = ["yes"], dictionary = ["not"]
# Output: []
# Explanation:
# Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.
 

# Constraints:

# 1 <= queries.length, dictionary.length <= 100
# n == queries[i].length == dictionary[j].length
# 1 <= n <= 100
# All queries[i] and dictionary[j] are composed of lowercase English letters.
# Accepted
# 18,537
# Submissions
# 30,736


class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        # Внутренняя функция для проверки совпадения двух слов после не более чем двух правок
        def isMatch(word1, word2):
            # Проверка, являются ли слова одинаковыми. Если да, то нет необходимости в правках.
            if word1 == word2:
                return True

            # Проверка, имеют ли слова одинаковую длину. Если нет, не удается преобразовать слово.
            if len(word1) != len(word2):
                return False

            # Подсчет различных символов между двумя словами.
            edit_count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    edit_count += 1
                    # Если количество правок превысит 2, слова не совпадают.
                    if edit_count > 2:
                        return False

            # Если ни одно из вышеуказанных условий не выполняется, слова считаются совпадающими.
            return True

        result = []  # Создаем пустой список для хранения совпадающих слов

        for query in queries:  # Перебираем слова из запросов
            matched = False  # Флаг для отслеживания совпадений
            for word in dictionary:  # Перебираем слова из словаря
                if isMatch(query, word):  # Проверяем, совпадают ли слова
                    matched = True  # Если есть совпадение, устанавливаем флаг
                    break  # Прерываем внутренний цикл

            if matched:
                result.append(query)  # Если нашлось совпадение, добавляем слово в результат

        return result  # Возвращаем список слов, которые соответствуют словам из словаря

list_q = ["word","note","ants","wood"], ["yes"]
list_d = ["wood","joke","moat"], ["not"]
for index, q in enumerate(list_q):
  Solution.twoEditWords('Success', q, list_d[index])
