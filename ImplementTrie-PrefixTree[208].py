# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.
# Accepted
# 789.3K
# Submissions
# 1.3M
# Acceptance Rate
# 62.6%
class Trie(object):

    def __init__(self):# Метод инициализации 
        self.trie = {} #Инициализируем Trie как пустой словарь

    def insert(self, word): # Метод вставляет строку word в Trie
        node = self.trie # Создаём ноду из словаря     
        for char in word: # Перебираем символы строки word
            
            if char not in node:# Если символ отсутствует в текущем узле
                node[char] = {} # Добавляем его и устанавливаем пустой словарь для этого символа
            node = node[char] # Переходим к следующему узлу
        node['$'] = True # Устанавливаем флаг конца слова в последнем узле
    def search(self, word):# Метод для поиска строки word в Trie
        node = self.trie # Создаём ноду из словаря     
        for char in word: # Перебираем символы строки word
            if char not in node: # Если символ отсутствует в текущем узле
                return False # Отсекаем с помощью False
            node = node[char] # Переходим к следующему узлу
        return '$' in node # Если флаг конца слова установлен, возвращаем True, иначе False

    def startsWith(self, prefix): #Метод для проверки, есть ли в Trie ранее вставленное слово, которое начинающееся с префикса prefix
        node = self.trie # Создаём ноду из словаря 
        for char in prefix: # Перебираем символы префикса
            if char not in node: # Если символ отсутствует в текущем узле
                return False # Отсекаем с помощью False
            node = node[char] # Переходим к следующему узлу
        return True # Возвращаем True, если есть хотя бы одно слово, которое начинается с префикса prefix



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
