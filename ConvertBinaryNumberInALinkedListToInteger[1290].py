# 1290. 
# Easy

# 3975

# 148

# Add to List

# Share
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

 

# Example 1:


# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
 

# Constraints:

# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
# Accepted
# 421,489
# Submissions
# 517,482


# Определение класса ListNode для представления узлов связанного списка.
# У каждого узла есть значение (val) и указатель на следующий узел (next).
# Если next равно None, то это последний узел в связанном списке.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        # Инициализируем переменную decimal_value для хранения десятичного значения.
        decimal_value = 0
        
        # Инициализируем переменную current для указания на текущий узел, начиная с головного узла.
        current = head

        # Пока текущий узел существует (не равен None):
        while current:
            # Сдвигаем текущее десятичное значение влево на 1 бит (умножение на 2)
            # и добавляем значение текущего узла (0 или 1) справа.
            decimal_value = (decimal_value << 1) | current.val
            
            # Переходим к следующему узлу в связанном списке.
            current = current.next

        # Возвращаем полученное десятичное значение после обработки всего связанного списка.
        return decimal_value

list_h = [1,0,1], [0]

for i in list_h:
   Solution.getDecimalValue('Success', i)
