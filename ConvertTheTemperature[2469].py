# Companies

# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

# Return the array ans. Answers within 10-5 of the actual answer will be accepted.

# Note that:

#     Kelvin = Celsius + 273.15
#     Fahrenheit = Celsius * 1.80 + 32.00

 

# Example 1:

# Input: celsius = 36.50
# Output: [309.65000,97.70000]
# Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.

# Example 2:

# Input: celsius = 122.11
# Output: [395.26000,251.79800]
# Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.

 

# Constraints:

#     0 <= celsius <= 1000

# Accepted
# 63.9K
# Submissions
# 71.6K
# Acceptance Rate
# 89.2%

class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin=celsius+273.15
        fahrenheit=(celsius*1.80)+32.00
        ans=[kelvin,fahrenheit]
        return ans
        # return [celsius + 273.15 , celsius *1.8 + 32]
    
cels_list = 36.50,122.11
for i in cels_list:
    Solution.convertTemperature('Success', i)