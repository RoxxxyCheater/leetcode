# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

 

# Constraints:

#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.

# Accepted
# 3.4M
# Submissions
# 8.5M
# Acceptance Rate
# 40.1%


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
list1 = [2,4,3],[0],[9,9,9,9,9,9,9]
list2 = [5,6,4],[0],[9,9,9,9]

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode

        :rtype: ListNode
        """
        

# Создаем новый связанный список, который будет содержать результат сложения
result = ListNode(0)
# Указатель на текущий узел в результирующем списке
curr = result
# Переменная для хранения "переноса" при сложении цифр
carry = 0

# Выполняем цикл, пока есть цифры для сложения или есть "перенос"
while l1 or l2 or carry:
    # Получаем значения текущих цифр из обоих списков или нули, если один из списков закончился
    x = l1.val if l1 else 0
    y = l2.val if l2 else 0
    # Вычисляем сумму текущих цифр и "переноса" от предыдущего шага
    summ = x + y + carry
    # Вычисляем новое значение "переноса" и значение цифры для нового узла результирующего списка
    carry, val = divmod(summ, 10)
    # Создаем новый узел с вычисленной цифрой и добавляем его в результирующий список
    curr.next = ListNode(val)
    # Перемещаем указатель текущего узла на только что созданный узел
    curr = curr.next
    # Переходим к следующим цифрам в обоих списках, если они есть
    if l1: l1 = l1.next
    if l2: l2 = l2.next

# Возвращаем начало списка, пропуская первый узел с нулевым значением
return result.next



        # not for Node List Solution
        # res = list(map(int,l1[::-1])) + list(map(int,l2[::-1]))
        # print(res, l1, l2)
        # return res, l1, l2

for i in range(len(list1)):
    Solution.addTwoNumbers(list1[i],list1[i], list2[i])
