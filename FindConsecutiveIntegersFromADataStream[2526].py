# 2526. Find Consecutive Integers from a Data Stream
# Medium

# For a stream of integers, implement a data structure that checks if the last k integers parsed in the stream are equal to value.

# Implement the DataStream class:

#     DataStream(int value, int k) Initializes the object with an empty integer stream and the two integers value and k.
#     boolean consec(int num) Adds num to the stream of integers. Returns true if the last k integers are equal to value, and false otherwise. If there are less than k integers, the condition does not hold true, so returns false.

 

# Example 1:

# Input
# ["DataStream", "consec", "consec", "consec", "consec"]
# [[4, 3], [4], [4], [4], [3]]
# Output
# [null, false, false, true, false]

# Explanation
# DataStream dataStream = new DataStream(4, 3); //value = 4, k = 3 
# dataStream.consec(4); // Only 1 integer is parsed, so returns False. 
# dataStream.consec(4); // Only 2 integers are parsed.
#                       // Since 2 is less than k, returns False. 
# dataStream.consec(4); // The 3 integers parsed are all equal to value, so returns True. 
# dataStream.consec(3); // The last k integers parsed in the stream are [4,4,3].
#                       // Since 3 is not equal to value, it returns False.

 

# Constraints:

#     1 <= value, num <= 109
#     1 <= k <= 105
#     At most 105 calls will be made to consec.

# Accepted
# 20,517
# Submissions
# 43,523

class DataStream(object):

    def __init__(self, value, k):
        """
        Инициализация объекта DataStream.
        
        :type value: int
            Значение, которое мы ищем в потоке.
        :type k: int
            Размер окна, в котором мы проверяем, что последние k чисел равны value.
        """
        self.value = value
        self.k = k
        self.stream = deque()           # Двусторонняя очередь для хранения последних k элементов потока.
        self.value_counter = Counter()   # Счетчик для подсчета количества вхождений значения в текущем окне.

    def consec(self, num):
        """
        Добавление числа в поток и проверка условия.
        
        :type num: int
            Добавляемое число в поток.
        :rtype: bool
            Возвращает True, если последние k чисел равны value, и False в противном случае.
        """
        self.stream.append(num)  # Добавляем число в конец очереди.

        if num == self.value:
            self.value_counter[num] += 1  # Увеличиваем счетчик для указанного значения.

        if len(self.stream) > self.k:
            leftmost = self.stream.popleft()  # Удаляем левый (старый) элемент из окна.
            self.value_counter[leftmost] -= 1  # Уменьшаем счетчик для удаленного значения.
            if self.value_counter[leftmost] == 0:
                del self.value_counter[leftmost]  # Удаляем из счетчика, если счетчик стал равен 0.

        return self.value_counter[self.value] == self.k  # Проверяем условие.



Your DataStream object will be instantiated and called as such:
obj = DataStream(value, k)
param_1 = obj.consec(num)
