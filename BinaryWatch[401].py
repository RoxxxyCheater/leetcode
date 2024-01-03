# 401. Binary Watch
# Easy

# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

#     For example, the below binary watch reads "4:51".

# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

# The hour must not contain a leading zero.

#     For example, "01:00" is not valid. It should be "1:00".

# The minute must consist of two digits and may contain a leading zero.

#     For example, "10:2" is not valid. It should be "10:02".

 

# Example 1:

# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

# Example 2:

# Input: turnedOn = 9
# Output: []

 

# Constraints:

#     0 <= turnedOn <= 10

# Accepted
# 135,404
# Submissions
# 252,988



class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        def count_bits(num):
            # Функция для подсчета количества включенных битов в числе
            return bin(num).count('1')

        result = []

        for hour in range(12):
            for minute in range(60):
                if count_bits(hour) + count_bits(minute) == turnedOn:
                    # Форматирование времени с использованием str.format()
                    result.append("{:d}:{:02d}".format(hour, minute))

        return result



l_t = 1, 9

for i in l_t:
   Solution.readBinaryWatch('Success', i)


