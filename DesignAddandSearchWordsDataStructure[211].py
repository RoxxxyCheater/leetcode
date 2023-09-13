# 211. Design Add and Search Words Data Structure
# Medium

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

#     WordDictionary() Initializes the object.
#     void addWord(word) Adds word to the data structure, it can be matched later.
#     bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

 

# Constraints:

#     1 <= word.length <= 25
#     word in addWord consists of lowercase English letters.
#     word in search consist of '.' or lowercase English letters.
#     There will be at most 2 dots in word for search queries.
#     At most 104 calls will be made to addWord and search.

# Accepted
# 557,788
# Submissions
# 1,257,245


class TrieNode:
    def __init__(self):
        # Инициализируем словарь для хранения дочерних узлов (букв)
        self.children = {}
        # Флаг, который указывает, является ли этот узел концом слова
        self.is_end_of_word = False

class WordDictionary(object):

    def __init__(self):
        # Инициализируем корень дерева Trie
        self.root = TrieNode()

    def addWord(self, word):
        """
        Добавляет слово в структуру данных Trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        # Проходим по каждой букве слова и строим соответствующие узлы Trie
        for char in word:
            if char not in node.children:
                # Если буква отсутствует в текущем узле, создаем новый узел для нее
                node.children[char] = TrieNode()
            # Переходим к следующему узлу в Trie
            node = node.children[char]
        # Помечаем конечный узел слова как конец слова
        node.is_end_of_word = True

    def search(self, word):
        """
        Поиск слова в структуре данных Trie с учетом символов '.'.
        :type word: str
        :rtype: bool
        """
        def dfs(node, index):
            if index == len(word):
                # Если мы достигли конца строки word, возвращаем флаг конца слова текущего узла Trie
                return node.is_end_of_word

            char = word[index]
            if char != '.':
                if char not in node.children:
                    # Если буква не найдена в дочерних узлах, возвращаем False
                    return False
                # Рекурсивно продолжаем поиск в следующем узле Trie
                return dfs(node.children[char], index + 1)
            else:
                # Если встречен символ '.', перебираем все дочерние узлы и ищем в них
                for child in node.children:
                    if dfs(node.children[child], index + 1):
                        # Если найдено совпадение в одном из дочерних узлов, возвращаем True
                        return True
                # Если ни в одном из дочерних узлов не найдено совпадение, возвращаем False
                return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
