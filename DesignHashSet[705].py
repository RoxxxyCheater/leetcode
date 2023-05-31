# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
 

# Constraints:

# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.
# Accepted
# 339,713
# Submissions
# 504,110
class MyHashSet(object):

    def __init__(self):
        self.hashset = [False] * 1000001  # Инициализация хэш-множества с заранее заданным размером

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset[key] = True  # Устанавливаем значение в индексе ключа равным True для указания наличия ключа

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset[key] = False  # Устанавливаем значение в индексе ключа равным False для указания удаления ключа

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.hashset[key]  # Возвращаем значение в индексе ключа для проверки наличия ключа


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
